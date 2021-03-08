var elements = document.evaluate("//*[contains(., 'Beat the par')]/ancestor::div[contains(concat(' ', @class, ' '), ' achieveRow ')][1]", document, null, XPathResult.ANY_TYPE, null);
removeElements();
var elements = document.evaluate("//*[contains(., 'Beat par')]/ancestor::div[contains(concat(' ', @class, ' '), ' achieveRow ')][1]", document, null, XPathResult.ANY_TYPE, null);
removeElements();
var elements = document.evaluate("//*[contains(., 'playlist')]/ancestor::div[contains(concat(' ', @class, ' '), ' achieveRow ')][1]", document, null, XPathResult.ANY_TYPE, null);
removeElements();
var elements = document.evaluate("//*[contains(., 'under 3 hours')]/ancestor::div[contains(concat(' ', @class, ' '), ' achieveRow ')][1]", document, null, XPathResult.ANY_TYPE, null);
removeElements();
var elements = document.evaluate("//*[contains(., 'multiplayer games')]/ancestor::div[contains(concat(' ', @class, ' '), ' achieveRow ')][1]", document, null, XPathResult.ANY_TYPE, null);
removeElements();

function removeElements() {
	var element = elements.iterateNext();
	var elem = [];
	console.log(element)

	while (element){

	  elem.push(element)
	  element = elements.iterateNext();
	}


	elem.forEach((element) => {
	  element.remove()
	})
}