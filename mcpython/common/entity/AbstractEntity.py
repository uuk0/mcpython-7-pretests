from abc import ABC

import mcpython.common.event.Registry


class AbstractEntity(mcpython.common.event.Registry.IRegistryContent, ABC):
    def on_summon(self):
        pass

    def can_be_killed_by_entity(self, entity: "AbstractEntity", item) -> bool:
        return True

    def on_kill(self):
        pass

    def on_player_interaction(
        self, player, ray_cast_result, button: int, modifiers: int
    ) -> bool:
        return False
