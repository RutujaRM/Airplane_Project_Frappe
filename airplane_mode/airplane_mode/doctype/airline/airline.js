// // Copyright (c) 2024, airplane_mode and contributors
// // For license information, please see license.txt


// frappe.ui.form.on('Airline', {
//     refresh: function(frm) {
//         if (frm.doc.website) {
//             // Add a link button to open the airline's website
//             frm.add_custom_button(__('Official Website'), function() {
//                 window.open(frm.doc.website, '_blank');
//             }).addClass('btn-primary');
//         }
//     },
// });



// To create website button on which we can go that particular airline official website

frappe.ui.form.on("Airline", {
	refresh(frm) {
        const website = frm.doc.website;
        frm.add_web_link(website, "Visit Website")

	},
});







