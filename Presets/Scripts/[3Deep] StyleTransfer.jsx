try{
    
    var doc = app.activeDocument;

    StyleTransferWindow = new Window ("dialog", "Style Transfer"); 
    StyleTransferWindow.orientation = "row";
    
    // not using {doc.path or doc.name} because it's not sure if the user will have a saved file or just a new window.
    var working_dir  = new File($.fileName).parent.fsName + "\\StyleTransfer";
    var styles_dir  = Folder(working_dir + "\\styles");

    function StartStyleTransfer() {
     
        var style_name = this.style.name.split(/(\\|\/)/g).pop();

        var temp_img_path = working_dir + "\\temp\\temp_img_for_styletransfer.jpg";
        var temp_batch_path = working_dir + "\\temp\\temp_batch_for_styletransfer.bat";

        var file = new File(temp_img_path)
        var opts = new JPEGSaveOptions();
        opts.quality = 10;
        doc.saveAs(file, opts, true);

        var batch_file = new File(temp_batch_path);
        batch_file.encoding = "UTF8";
        batch_file.open("e", "TEXT", "????");
        batch_file.writeln("python \"" + working_dir + "\\style_transfer.py\" \"" + working_dir + "\\models\\" + style_name + "\" \"" + temp_img_path + "\"");
        batch_file.close();

        StyleTransferWindow.close();
        batch_file.execute();

     }

    if(styles_dir.exists)
    {
            style_files = styles_dir.getFiles();
            
            for (var style in style_files)
            {
                var style_btn = StyleTransferWindow.add("iconbutton", undefined, style_files[style]);
                style_btn.style = style_files[style];
                style_btn.onClick = StartStyleTransfer;
            }
            
    }

    StyleTransferWindow.show();

}
catch(error){
    alert("No opened document found, please open a file and run the script again.");
}