#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import gi
gi.require_version('Gimp', '3.0')
from gi.repository import Gimp, GLib, GObject

class AddGuides3366(Gimp.PlugIn):
   
    __gtype_name__ = "add_guides_33_66"
    
    def do_set_i18n(self, procname):
        # Desactivar localización para evitar advertencias
        return False, 'gimp30-python', None
    
    def do_query_procedures(self):
        return ['python-fu-add-guides-33-66']
    
    def do_create_procedure(self, name):
        procedure = Gimp.ImageProcedure.new(
            self, name,
            Gimp.PDBProcType.PLUGIN,
            self.run, None
        )
        
        procedure.set_image_types("*")
        procedure.set_sensitivity_mask(Gimp.ProcedureSensitivityMask.DRAWABLE)
        procedure.set_menu_label("Add Guides 33-66%")
        procedure.add_menu_path('<Image>/Image/Guides/')
        
        procedure.set_documentation(
            "Add guides at 33% and 66%",
            "Adds 4 guides: vertical at 33% and 66%, horizontal at 33% and 66%",
            name
        )
        procedure.set_attribution("Gezzer Garcia", "Gezzer Garcia", "2025")
        
        return procedure
    
    def run(self, procedure, run_mode, image, drawables, config, run_data):
        # Iniciar grupo de deshacer
        image.undo_group_start()
        
        try:
            # Obtener dimensiones de la imagen
            width = image.get_width()
            height = image.get_height()
            
            # Calcular posiciones
            v1 = int(width * 0.3333)
            v2 = int(width * 0.6666)
            h1 = int(height * 0.3333)
            h2 = int(height * 0.6666)
            
            # Añadir guías verticales (posiciones x)
            image.add_vguide(v1)
            image.add_vguide(v2)
            
            # Añadir guías horizontales (posiciones y)
            image.add_hguide(h1)
            image.add_hguide(h2)
            
            # Finalizar grupo de deshacer
            image.undo_group_end()
            
            # Actualizar displays
            Gimp.displays_flush()
            
            return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, GLib.Error())
            
        except Exception as e:
            # Capturar cualquier error
            Gimp.message(f"ERROR: {str(e)}")
            image.undo_group_end()
            
            error = GLib.Error()
            return procedure.new_return_values(Gimp.PDBStatusType.EXECUTION_ERROR, error)

# Punto de entrada principal
Gimp.main(AddGuides3366.__gtype_name__, sys.argv)
