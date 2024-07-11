
// To Add inner button to this doctype which having and option to assign seat to that particular ticket 

frappe.ui.form.on("Airplane Ticket", 
    {
	refresh(frm)  // refresh event callback function when from is refresh
     {
        frm.page.add_inner_button(__('Assign Seat'), function()  //Add a button to the inner toolbar of the form
        {
            frappe.prompt([ //prompt dialog to get seat number input from the user
                {
                    fieldname: 'seat_number',
                    fieldtype: 'Data',
                    label: __('Seat Number'),
                    reqd: 1                    //To make it mandatory
                }
            ], function(values) //To execute when the button is clicked
            {
                frm.set_value('seat', values.seat_number);  //Assign the value which enter into promt to seat field
            }, __('Select Seat'), __('Assign')); //Title prompt , assign button
        }, __("Action"), "btn-primary");


	},
});

