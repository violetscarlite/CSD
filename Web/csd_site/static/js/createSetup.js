var numOfData = -1;
var dataSetups = [];

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
    draggable.slideUp(function() {
    	droppable.find('.groupData').append(draggable);
        draggable.slideDown();
    });
}

function changeGroup( event, ui){
    var draggable = ui.item;
    var droppable = $(this);
    var sender = ui.sender;
    var name = "default"

    if(droppable.hasClass('singleGroup')){
        name = droppable.find('.groupName').val();
    }

    draggable.find('.group').val(name);
}

function addData(){
	numOfData += 1;
    dataSetups.push(numOfData)
    var html =$('#' + $('.sidebar .dataType').val() + 'HTML').html().replace(/numOfData/g, numOfData);
    $('#default').append(html);
    var div = $('#default .singleSetupDiv:last');
    div.find('.longName').val($('.sidebar .dataLong').val());
    div.find('.shortName').val($('.sidebar .dataShort').val());
    div.find('.type').val($('.sidebar .dataType').val());
    //div.find('.title').html(div.find('.longName').val());

    // div.draggable({
    //     helper: 'clone',
    //     opacity: .73,
    // });
    div.slideDown(400);
    div.find('.closeButton').click(function(){
        $(this).closest('.singleSetupDiv').slideUp(400, function(){
            var index = dataSetups.indexOf($(this).find('numberOfData').val())
            dataSetups.splice(index,1);
            $(this).remove();

        });
        return;
    });
    div.find('.toggleDisplay').click( function() {
        return minimizeToggle(this,'.singleSetupDiv','.dataDiv');});
    div.find('.title').html(div.find('.nameInput').val());
    div.find('.longName').keyup(function() {
        $(this).closest('.singleSetupDiv').find('.title').html($(this).val());
    });
    div.find('.longName').keyup(); 

    $( ".sortable" ).sortable( "refresh" );
    return false;
}

function addGroup(){
	$('#groups').append($('#groupHTML').html());
    var div = $('#groups .singleGroup:last');
    div.find('.groupName').val($('.sidebar .groupLong').val());
    div.find('.toggleDisplay').click(function(){return minimizeToggle(this,'.singleGroup','.groupData');});
    div.slideDown(400);
    div.find('.closeButton').click(function() {
        $(this).closest(".singleGroup").parent().slideUp(400,function(){
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

    //div.droppable({
    //   drop: groupDropEvent,
    //  tolerance: "pointer",
    //});
    // div.find('.sortable').sortable({
    div.sortable({
        tolerance: 'pointer',
        helper: 'clone',
        connectWith: '.sortable',
        items: '.singleSetupDiv',
        over: changeGroup,
        opacity: .73,
        distance: 10,
    })

    return false;
}

$(document).ready(function(){
    /*$('.addData').click(function(){
    	addData();
    });

    $('.addGroup').click(function() {
        addGroup();
    });*/  

    $('#addDataForm').submit(function(){
        return addData();    
    });

    $('.sortable').sortable({
        tolerance: 'pointer',
        helper: 'clone',
        connectWith: '.sortable',
        items: '.singleSetupDiv',
        over: changeGroup,
        opacity: .73,
        distance: 10,
    });

    $('#submitSetupBtn').click(function() {
        $('#setupForm').append('<input type="hidden" name="dataSetups" value="' + dataSetups.toString() + '"/>');
        $('#setupForm').append('<input type="hidden" name="competition" value="' + $('#competitions option:selected').val() + '"/>');
        $('#setupForm').submit();
    });
});