"ui";
var m = device.width;
showmainUi();
function showmainUi(){
ui.layout(
  <drawer>
  <vertical>
    <appbar>
        <toolbar id="toolbar" />
        <tabs id="tabs" />
    </appbar>
    <frame marginTop="10">
      <button w="40" h="40" id="start" layout_gravity="center" bg="file:///storage/emulated/0/Pictures/播放.png"/>
    </frame>
</vertical>
</drawer>    
);
ui.emitter.on("create_options_menu",menu=>{
  menu.add("设置");
  menu.add("关于");
});
ui.toolbar.setupWithDrawer(ui.drawer);
}