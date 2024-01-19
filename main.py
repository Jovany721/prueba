import flet as ft
import time

def main(page: ft.Page):



    def pick_files_result2(e: ft.FilePickerResultEvent):
        a = e.files
        try:
            primera_instancia =a[0]
            openn = open(f'{primera_instancia.path}', 'r')
            area_texto.value = openn.read()
            area_texto.update()
        except:
            None

      



    def pick_files_result(e: ft.FilePickerResultEvent):

        texto = open(f'{e.path}.txt', 'w')
        texto.write(area_texto.value)
 
    def funcion (a):
        if a==0:
            file_picker.save_file(allowed_extensions=['txt'])

        if a == 1:
            
            file_picker2.pick_files(allowed_extensions=["txt"])

        







    file_picker = ft.FilePicker(on_result=pick_files_result)
    page.overlay.append(file_picker)
    page.update()



    file_picker2 = ft.FilePicker(on_result=pick_files_result2)
    page.overlay.append(file_picker2)
    page.update()


        
 

    rail = ft.NavigationRail(
        selected_index=0,
        label_type=ft.NavigationRailLabelType.ALL,
        min_width=100,
        min_extended_width=200,
        group_alignment=-0.9,
        bgcolor=ft.colors.WHITE,



        destinations=[
            ft.NavigationRailDestination(
                 selected_icon=ft.icons.ARCHIVE, label="guardar"),
                
            ft.NavigationRailDestination(
                 selected_icon=ft.icons.FILE_OPEN, label="Abrir"),


             ft.NavigationRailDestination(
                icon_content=ft.Icon(ft.icons.BOOKMARK_BORDER),
                selected_icon_content=ft.Icon(ft.icons.BOOKMARK),
                label="Second")



        ],
       on_change=lambda e:funcion(e.control.selected_index )
    
    )
    area_texto = ft.TextField( multiline= True, text_style=ft.TextStyle(color='black'), border_color=ft.colors.GREY_100)













    page.add(
        ft.Row(
            [
               ft.Container( rail,bgcolor=ft.colors.TRANSPARENT),
                ft.VerticalDivider(width=1),
               ft.Container( area_texto, width='545', height='1000')
            ],
            expand=True,
        )
    )

ft.app(target=main)