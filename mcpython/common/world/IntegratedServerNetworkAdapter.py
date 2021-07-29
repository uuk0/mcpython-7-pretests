"""
An adapter for local lan worlds which use by the nature of them a IntegratedWorld but need to sync stuff
via the network to a client using a ClientWorld

This provides a wrapper layer around the internal IntegratedWorld doing all the stuff a ServerWorld would do
to make things work

It needs to bind itself to certain updates via a local event system

WARNING: local LAN worlds are not as good as real servers! You are mixing two different implementations!

As a mod author wanting to fix this, replace the side_world in the network manager
"""
