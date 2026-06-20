"""
Chapter 17: Mini Project - Configuration Manager
Demonstrates class methods, static methods, and properties to manage application state safely.
"""

class AppConfig:
    """A singleton-like configuration manager."""
    
    # Internal class-level state
    _settings = {
        "debug_mode": False,
        "max_connections": 10
    }
    
    @classmethod
    def load_from_dict(cls, data: dict) -> None:
        """Loads configuration from a dictionary."""
        for key, value in data.items():
            # Only update known settings to prevent bloat
            if key in cls._settings:
                cls._settings[key] = value

    @classmethod
    def get(cls, key: str, default=None):
        """Safely retrieves a configuration value."""
        return cls._settings.get(key, default)

    @staticmethod
    def is_valid_port(port: int) -> bool:
        """
        A utility method that doesn't need class or instance state,
        but logically belongs in the config module.
        """
        return 0 <= port <= 65535

def main():
    print("--- Default Config ---")
    print(f"Debug: {AppConfig.get('debug_mode')}")
    print(f"Connections: {AppConfig.get('max_connections')}")
    
    print("\n--- Loading New Config ---")
    new_settings = {
        "debug_mode": True,
        "max_connections": 100,
        "unknown_key": "ignored"
    }
    AppConfig.load_from_dict(new_settings)
    
    print(f"Debug: {AppConfig.get('debug_mode')}")
    print(f"Connections: {AppConfig.get('max_connections')}")
    print(f"Unknown Key: {AppConfig.get('unknown_key')}")
    
    print("\n--- Static Utility ---")
    print(f"Is 8080 a valid port? {AppConfig.is_valid_port(8080)}")
    print(f"Is 99999 a valid port? {AppConfig.is_valid_port(99999)}")

if __name__ == "__main__":
    main()
