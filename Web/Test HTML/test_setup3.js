var numOfData = -1;

function minimizeToggle(button, parentDiv, toggleDiv) {
	$(button).closest(parentDiv).find(toggleDiv).slideToggle(400);
	$(button).find(".icon-plus").toggle();
	$(button).find(".icon-minus").toggle();
	return false;
}

function groupDropEvent( event, ui){
    var draggable = ui.draggable;
    var droppable = $(this);

    draggable.find('.group').val(droppable.find('.groupName').val());
    //draggable.remove();
    draggable.slideUp(function() {
    	droppable.find('.groupData').append(draggable);
    	draggable.slideDown();
    });
}

function addData(){
	numOfData += 1;
    var html =$('#' + $('.sidebar .dataType').val() + 'HTML').html().replace(/numOfData/g, numOfData);
    $('#default').append(html);
    var div = $('#default .singleSetupDiv:last');
    div.find('.longName').val($('.sidebar .dataLong').val());
    div.find('.shortName').val($('.sidebar .dataShort').val());
    div.find('.type').val($('.sidebar .dataType').val());
    //div.find('.title').html(div.find('.longName').val());

    div.draggable({
        helper: 'clone',
        opacity: .73,
    });
    div.slideDown(400);
    div.find('.closeButton').click(function(){
        $(this).closest('.singleSetupDiv').slideUp(400, function(){
            $(this).remove();
        });
        return;
    });
    div.find('.toggleDisplay').click( function() {minimizeToggle(this,'.singleSetupDiv','.dataDiv');});
    div.find('.title').html(div.find('.nameInput').val());
    div.find('.longName').keyup(function() {
        $(this).closest('.singleSetupDiv').find('.title').html($(this).val());
    });
    div.find('.longName').keyup(); 

    return false;
}

function addGroup(){
	$('#groups').append($('#groupHTML').html());
    var div = $('#groups .singleGroup:last');
    div.find('.groupName').val($('.sidebar .groupLong').val());
    div.find('.toggleDisplay').click(function(){minimizeToggle(this,'.singleGroup','.groupData');});
    div.slideDown(400);
    div.find('.closeButton').click(function() {
        $(this).closest(".singleGroup").slideUp(400,function(){
            $(this).remove();
        });
    });
    div.find('.editButton').click(function() {
        var input = $(this).closest(".singleGroup").find(".groupName")
        input.prop("disabled",false);
        input.focus();
        
        return false;
    });
    var input = div.find(".groupName");
    input.keypress(function(event) {
        if(event.which == 13){
            $(this).blur();
        }
    });
    input.blur(function() {
        console.log("lost focus");
        var name = $(this).val();
        $(this).prop("disabled",true);
        $(this).closest('singleGroup').find('.group').each(function() {
        	$(this).val(name);
        });
    });

    div.droppable({
        drop: groupDropEvent,
        tolerance: "pointer",
    });

    return false;
}

$(document).ready(function(){
    /*$('.addData').click(function(){
    	addData();
    });

    $('.addGroup').click(function() {
        addGroup();
    });*/       
});