# -*- mode: python; python-indent: 4 -*-
import ncs
from ncs.application import Service
import paramiko
from scp import SCPClient

class CopyFile(Action):
    '''Test the connectivity with Ping from A devices the B devices both from
       over the regular interface and the Tunnel'''
    @Action.action
    def cb_action(self, uinfo, name, kp, input, output):
        self.log.info('action name: ', name, " ", kp)
        device = ncs.maagic.get_node(trans, kp)
        self.log.info('action name: ', device.name)

        # ssh = createSSHClient(server, port, user, password)
        # scp = SCPClient(ssh.get_transport())

def createSSHClient(server, port, user, password):
    client = paramiko.SSHClient()
    client.load_system_host_keys()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server, port, user, password)
    return client



# ---------------------------------------------
# COMPONENT THREAD THAT WILL BE STARTED BY NCS.
# ---------------------------------------------
class Main(ncs.application.Application):
    def setup(self):
        # The application class sets up logging for us. It is accessible
        # through 'self.log' and is a ncs.log.Log instance.
        self.log.info('Main RUNNING')

        # Service callbacks require a registration for a 'service point',
        # as specified in the corresponding data model.
        #
        self.register_action('cisco-asa-vpn-copy-file', CopyFile)

        # If we registered any callback(s) above, the Application class
        # took care of creating a daemon (related to the service/action point).

        # When this setup method is finished, all registrations are
        # considered done and the application is 'started'.

    def teardown(self):
        # When the application is finished (which would happen if NCS went
        # down, packages were reloaded or some error occurred) this teardown
        # method will be called.

        self.log.info('Main FINISHED')
