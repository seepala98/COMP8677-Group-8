const units = {
	Luman: '',
};

const config = {
	minLuman: 0,
	maxLuman: 100,
	unit: "Luman"
};

// Change min and max brightness values

const tempValueInputs = document.querySelectorAll("input[type='text']");

tempValueInputs.forEach((input) => {
	input.addEventListener("change", (event) => {
		const newValue = event.target.value;

		if(isNaN(newValue)) {
			return input.value = config[input.id];
		} else {
			config[input.id] = input.value;
			range[input.id.slice(0, 3)] = config[input.id]; // Update range
			return renderBrightness(); // Update brightness
		}
	});
});

// Change brightness

let range = document.querySelector("input[type='range']");
const brightness = document.getElementById("brightness");

function renderBrightness() {
	brightness.innerHTML = range.value + units[config.unit];
	brightness.dataset.value = range.value + units[config.unit];
}

function updateBrightness() {
	$.get('/password', function(data) {
		$.post('/brightness?value=' + range.value + '&password=' + data.password, function(data) {
			console.debug('response from the server: ');
			console.debug(data);
			renderBrightness();
		});
	});
}

range.addEventListener("input", updateBrightness);


function pollBrightness() {
	$.get('/brightness', function(data) {
		if (!data.hasOwnProperty('brightness')) {
			console.error('server does not send the correct data');
		} else {
			let newBrightness = data.brightness;
			if (newBrightness !== Number(range.value)) {
				console.log('newBrightness is [' + newBrightness + '], range.value is [' + range.value + ']');
				console.log('set brightness to ' + newBrightness + ' as informed by the server.');
				range.value = newBrightness;
			}
			renderBrightness();
		}
	});
}

setInterval(pollBrightness, 1000);
