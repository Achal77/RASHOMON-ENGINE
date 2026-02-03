class ConflictDetector:
    def analyze(self, audio_text, visual_text):
        print("[-] Analyzing Consistency...")
        
        conflicts = []
        # Simple Logic: If audio says 'gun' but video sees 'phone'
        if "gun" in audio_text.lower() and "phone" in visual_text.lower():
            conflicts.append("CRITICAL CONFLICT: Audio implies weapon; Video confirms benign object.")
        
        if not conflicts:
            return "No conflicts detected. Narratives align."
        return conflicts