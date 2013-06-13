//Example for ajax login

// $(window).load(function(){                                                                                                                  
//  	$('#login_form').submit(function(e){                                                                                                        
//              e.preventDefault();                                                                                                             
//      var request_url = document.getElementById('next').value                                                                             
//           $.ajax({                                                                                                                           
//             type:"POST",                                                                                                                    
//              url: $(this).attr('action'),                                                                                                    
//              data: $('#login_form').serialize(),                                                                                             
//              success: function(response){ $('#msg').text(response);                                                                          
//              console.log(response);                                                                                                          
//              },                                                                                                                              
//              error: function(xhr, ajaxOptions, thrownError){ alert( $('#login_error').text('Username already taken. Please select another one.')}, 
//            });                                                                                                                               
//      });                                                                                                                                     
// }); 