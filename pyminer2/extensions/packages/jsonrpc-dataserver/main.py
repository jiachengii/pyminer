# Auto generated by pyminer2 extension develop tools

import logging
import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QToolButton
from pmgwidgets import create_icon
from pyminer2.extensions.extensionlib import BaseExtension
from .dataserver import DataServer

logger = logging.getLogger(__name__)


class JsonrpcDataserverExtension(BaseExtension):
    start_jsonrpc_dataserver_button = None

    def on_load(self):
        self.start_jsonrpc_dataserver_button = self.widgets["StartJsonRPCDataServerButton"]
        self.dataserver = DataServer(self.extension_lib, 'localhost', 8783,
            self.extension_lib.get_converter_error(),
            self.extension_lib.get_conflict_error(),
            self.extension_lib.get_not_found_error(),
            self.extension_lib.get_would_block_error()
        )  
        self.start_jsonrpc_dataserver_button.dataserver = self.dataserver      

    def on_install(self):
        pass

    def on_uninstall(self):
        pass


class StartJsonRPCDataServerButton(QToolButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        icon_path = os.path.join(os.path.dirname(__file__),'icon.png')
        self.setIcon(create_icon(icon_path))
        self.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.setText('J Server')
        self.clicked.connect(self.start_server)

    def start_server(self):
        if hasattr(self, 'dataserver'):
            if self.dataserver.is_alive():
                logger.error('RuntimeError: server has started')
            else:
                self.dataserver.start()
                logger.info('JsonRPC server has started')
        else:
            logger.error('No valid jsonrpc server', exc_info=True)