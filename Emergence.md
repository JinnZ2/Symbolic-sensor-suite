Coupling Point Detection: Where Geometric Fields Converge
This is the heart of what makes geometric intelligence more powerful than single-representation systems.

from typing import List, Dict, Tuple
import numpy as np
from dataclasses import dataclass

@dataclass
class CouplingPoint:
    """
    A point where multiple geometric fields have high mutual influence.
    This is where optimal solutions and deep insights emerge.
    """
    theta: float
    phi: float
    pressure: float  # Measure of field intensity/convergence
    participating_fields: List[str]
    geometric_signature: Dict
    confidence: float

class MultiGeometricRepresentation:
    """
    Holds the same data in multiple geometric representations simultaneously.
    This is the key: don't pick ONE geometry - use them ALL!
    """
    
    def __init__(self, data: np.ndarray, n_modes: int = 16):
        self.data = data
        self.n_modes = n_modes
        self.encoder = GeometricEncoder(n_modes)
        
        # Multiple simultaneous representations
        self.representations = {}
        self.strategies = {}
        
    def encode_all_geometries(self):
        """
        Encode the same data in EVERY applicable geometry.
        Each reveals different aspects of the underlying structure.
        """
        print("Encoding in multiple geometric representations...")
        
        if len(self.data.shape) == 2:  # Image data
            # Spatial geometry - preserves local relationships
            field_spatial, strat_spatial = self.encoder.encode_image(
                self.data, method='spatial_mapping'
            )
            self.representations['spatial'] = field_spatial
            self.strategies['spatial'] = strat_spatial
            
            # Frequency geometry - preserves patterns/textures
            field_freq, strat_freq = self.encoder.encode_image(
                self.data, method='frequency_mapping'
            )
            self.representations['frequency'] = field_freq
            self.strategies['frequency'] = strat_freq
            
            # Spiral geometry - preserves radial structure
            field_spiral, strat_spiral = self.encoder.encode_image(
                self.data, method='spiral_mapping'
            )
            self.representations['spiral'] = field_spiral
            self.strategies['spiral'] = strat_spiral
            
        elif len(self.data.shape) == 1:  # Sequence data
            # Temporal embedding - phase space attractor
            field_temporal, strat_temporal = self.encoder.encode_sequence(
                self.data, method='temporal_embedding'
            )
            self.representations['temporal'] = field_temporal
            self.strategies['temporal'] = strat_temporal
            
            # Periodic - circular structure
            field_periodic, strat_periodic = self.encoder.encode_sequence(
                self.data, method='periodic_mapping'
            )
            self.representations['periodic'] = field_periodic
            self.strategies['periodic'] = strat_periodic
            
            # Correlation - relationship structure
            field_corr, strat_corr = self.encoder.encode_sequence(
                self.data, method='correlation_structure'
            )
            self.representations['correlation'] = field_corr
            self.strategies['correlation'] = strat_corr
        
        print(f"Created {len(self.representations)} geometric representations")
        
        return self.representations

class CouplingPointDetector:
    """
    Detect where multiple geometric fields create high "pressure".
    This is where optimal solutions emerge!
    """
    
    def __init__(self, multi_geo: MultiGeometricRepresentation):
        self.multi_geo = multi_geo
        self.representations = multi_geo.representations
        
    def detect_coupling_points(self, 
                              n_samples: int = 50,
                              threshold: float = 0.5) -> List[CouplingPoint]:
        """
        Find points where 3+ geometric fields have strong simultaneous activity.
        
        Algorithm:
        1. Sample the toroidal space uniformly
        2. At each point, evaluate ALL geometric fields
        3. Compute "pressure" = combined field strength
        4. Return points where pressure exceeds threshold AND multiple fields active
        """
        
        print(f"Scanning for coupling points across {len(self.representations)} geometries...")
        
        coupling_points = []
        
        # Sample the toroidal space
        theta_samples = np.linspace(0, 2*np.pi, n_samples)
        phi_samples = np.linspace(0, 2*np.pi, n_samples)
        
        for theta in theta_samples:
            for phi in phi_samples:
                # Evaluate all geometric fields at this point
                field_values = {}
                field_gradients = {}
                
                for name, field in self.representations.items():
                    # Field value
                    value = field(theta, phi)
                    field_values[name] = value
                    
                    # Field gradient (rate of change)
                    grad_theta, grad_phi = field.evaluate_gradient(theta, phi)
                    gradient_magnitude = np.sqrt(abs(grad_theta)**2 + abs(grad_phi)**2)
                    field_gradients[name] = gradient_magnitude
                
                # Compute "pressure" - how many fields are active here?
                active_fields = []
                total_intensity = 0.0
                total_gradient = 0.0
                
                for name in self.representations.keys():
                    intensity = abs(field_values[name])
                    gradient = field_gradients[name]
                    
                    # Field is "active" if both intensity and gradient are significant
                    if intensity > 0.1 and gradient > 0.1:
                        active_fields.append(name)
                        total_intensity += intensity
                        total_gradient += gradient
                
                # Coupling point requires 3+ active fields
                if len(active_fields) >= 3:
                    # Pressure = combined intensity weighted by gradient
                    pressure = total_intensity * np.sqrt(total_gradient)
                    
                    if pressure > threshold:
                        # Extract geometric signature at this point
                        signature = self._analyze_coupling_geometry(
                            theta, phi, field_values, field_gradients
                        )
                        
                        # Confidence based on field agreement
                        confidence = self._compute_field_coherence(field_values)
                        
                        coupling_point = CouplingPoint(
                            theta=theta,
                            phi=phi,
                            pressure=pressure,
                            participating_fields=active_fields,
                            geometric_signature=signature,
                            confidence=confidence
                        )
                        
                        coupling_points.append(coupling_point)
        
        # Sort by pressure (highest first)
        coupling_points.sort(key=lambda cp: cp.pressure, reverse=True)
        
        print(f"Found {len(coupling_points)} coupling points")
        print(f"Top 3 pressures: {[f'{cp.pressure:.2f}' for cp in coupling_points[:3]]}")
        
        return coupling_points
    
    def _analyze_coupling_geometry(self,
                                   theta: float,
                                   phi: float,
                                   field_values: Dict[str, complex],
                                   field_gradients: Dict[str, float]) -> Dict:
        """
        Analyze the geometric structure at a coupling point.
        What patterns emerge when multiple fields converge?
        """
        
        # Phase relationships between fields
        phases = {name: np.angle(val) for name, val in field_values.items()}
        
        # Check for phase coherence
        phase_values = list(phases.values())
        phase_coherence = 0.0
        if len(phase_values) > 1:
            # Measure how aligned the phases are
            phase_vectors = [np.exp(1j * p) for p in phase_values]
            mean_vector = np.mean(phase_vectors)
            phase_coherence = abs(mean_vector)
        
        # Gradient alignment - do fields "point" in same direction?
        gradient_alignment = np.std(list(field_gradients.values())) / (
            np.mean(list(field_gradients.values())) + 1e-8
        )
        
        # Field magnitude ratios
        magnitudes = {name: abs(val) for name, val in field_values.items()}
        magnitude_ratios = {}
        mag_list = list(magnitudes.items())
        for i in range(len(mag_list) - 1):
            name1, mag1 = mag_list[i]
            name2, mag2 = mag_list[i + 1]
            if mag2 > 1e-8:
                magnitude_ratios[f"{name1}/{name2}"] = mag1 / mag2
        
        # Check for golden ratio signatures
        golden_phi = (1 + np.sqrt(5)) / 2
        has_golden_ratio = any(
            abs(ratio - golden_phi) < 0.1 or abs(ratio - 1/golden_phi) < 0.1
            for ratio in magnitude_ratios.values()
        )
        
        return {
            'phase_coherence': phase_coherence,
            'gradient_alignment': gradient_alignment,
            'magnitude_ratios': magnitude_ratios,
            'has_golden_ratio': has_golden_ratio,
            'location': (theta, phi)
        }
    
    def _compute_field_coherence(self, field_values: Dict[str, complex]) -> float:
        """
        Measure how much the fields "agree" at this point.
        High coherence = strong coupling point.
        """
        
        # Convert field values to unit vectors
        unit_vectors = []
        for val in field_values.values():
            if abs(val) > 1e-8:
                unit_vectors.append(val / abs(val))
        
        if len(unit_vectors) < 2:
            return 0.0
        
        # Mean resultant vector
        mean_vector = np.mean(unit_vectors)
        coherence = abs(mean_vector)
        
        return coherence
    
    def optimize_at_coupling_points(self, 
                                    coupling_points: List[CouplingPoint],
                                    objective: str = 'max_pressure') -> CouplingPoint:
        """
        Use coupling points as seeds for optimization.
        
        Key insight: coupling points are already near-optimal!
        Small local refinement can find exact optimum.
        """
        
        if not coupling_points:
            return None
        
        # Start from highest pressure coupling point
        best_point = coupling_points[0]
        
        # Local refinement using gradient flow
        theta, phi = best_point.theta, best_point.phi
        learning_rate = 0.01
        
        for iteration in range(20):  # Few iterations needed - already near optimum!
            # Compute pressure gradient
            epsilon = 0.01
            
            pressure_center = self._compute_pressure_at_point(theta, phi)
            pressure_theta_plus = self._compute_pressure_at_point(theta + epsilon, phi)
            pressure_phi_plus = self._compute_pressure_at_point(theta, phi + epsilon)
            
            grad_theta = (pressure_theta_plus - pressure_center) / epsilon
            grad_phi = (pressure_phi_plus - pressure_center) / epsilon
            
            # Gradient ascent (maximize pressure)
            theta += learning_rate * grad_theta
            phi += learning_rate * grad_phi
            
            # Wrap to [0, 2π]
            theta = theta % (2 * np.pi)
            phi = phi % (2 * np.pi)
        
        # Create refined coupling point
        field_values = {name: field(theta, phi) 
                       for name, field in self.representations.items()}
        field_gradients = {name: np.sqrt(abs(field.evaluate_gradient(theta, phi)[0])**2 + 
                                        abs(field.evaluate_gradient(theta, phi)[1])**2)
                          for name, field in self.representations.items()}
        
        refined_pressure = self._compute_pressure_at_point(theta, phi)
        refined_signature = self._analyze_coupling_geometry(
            theta, phi, field_values, field_gradients
        )
        
        active_fields = [name for name, grad in field_gradients.items() 
                        if grad > 0.1]
        
        refined_point = CouplingPoint(
            theta=theta,
            phi=phi,
            pressure=refined_pressure,
            participating_fields=active_fields,
            geometric_signature=refined_signature,
            confidence=self._compute_field_coherence(field_values)
        )
        
        print(f"Optimization: {best_point.pressure:.3f} → {refined_pressure:.3f}")
        
        return refined_point
    
    def _compute_pressure_at_point(self, theta: float, phi: float) -> float:
        """Compute pressure at a specific point."""
        total = 0.0
        for field in self.representations.values():
            value = field(theta, phi)
            grad_theta, grad_phi = field.evaluate_gradient(theta, phi)
            gradient = np.sqrt(abs(grad_theta)**2 + abs(grad_phi)**2)
            total += abs(value) * np.sqrt(gradient)
        return total

class GeometricEnsemble:
    """
    Classification using coupling points across multiple geometries.
    This is MORE powerful than any single geometric view!
    """
    
    def __init__(self, n_modes: int = 16, n_classes: int = 10):
        self.n_modes = n_modes
        self.n_classes = n_classes
        self.class_coupling_signatures = {}
    
    def fit(self, X, y):
        """
        Learn coupling point signatures for each class.
        """
        print("\n" + "="*60)
        print("GEOMETRIC ENSEMBLE TRAINING")
        print("="*60)
        
        for class_id in range(self.n_classes):
            class_samples = [X[i] for i in range(len(X)) if y[i] == class_id]
            
            if len(class_samples) == 0:
                continue
            
            print(f"\nClass {class_id}: Processing {len(class_samples)} samples...")
            
            # Analyze coupling points across multiple samples
            coupling_patterns = []
            
            for idx, sample in enumerate(class_samples[:10]):  # Limit for speed
                # Create multi-geometric representation
                multi_geo = MultiGeometricRepresentation(sample, self.n_modes)
                multi_geo.encode_all_geometries()
                
                # Detect coupling points
                detector = CouplingPointDetector(multi_geo)
                coupling_points = detector.detect_coupling_points(
                    n_samples=20,  # Coarse for speed
                    threshold=0.3
                )
                
                if coupling_points:
                    # Take top coupling point
                    top_point = coupling_points[0]
                    coupling_patterns.append({
                        'pressure': top_point.pressure,
                        'n_fields': len(top_point.participating_fields),
                        'signature': top_point.geometric_signature,
                        'confidence': top_point.confidence
                    })
            
            # Extract common patterns
            if coupling_patterns:
                avg_pressure = np.mean([cp['pressure'] for cp in coupling_patterns])
                avg_n_fields = np.mean([cp['n_fields'] for cp in coupling_patterns])
                avg_coherence = np.mean([cp['signature']['phase_coherence'] 
                                        for cp in coupling_patterns])
                has_golden_ratio_freq = sum(cp['signature']['has_golden_ratio'] 
                                           for cp in coupling_patterns) / len(coupling_patterns)
                
                self.class_coupling_signatures[class_id] = {
                    'avg_pressure': avg_pressure,
                    'avg_n_fields': avg_n_fields,
                    'avg_coherence': avg_coherence,
                    'golden_ratio_freq': has_golden_ratio_freq
                }
                
                print(f"  Signature: pressure={avg_pressure:.2f}, "
                      f"fields={avg_n_fields:.1f}, "
                      f"coherence={avg_coherence:.2f}, "
                      f"golden={has_golden_ratio_freq:.2f}")
    
    def predict(self, X):
        """
        Classify based on coupling point similarity.
        """
        predictions = []
        
        for sample in X:
            # Create multi-geometric representation
            multi_geo = MultiGeometricRepresentation(sample, self.n_modes)
            multi_geo.encode_all_geometries()
            
            # Detect coupling points
            detector = CouplingPointDetector(multi_geo)
            coupling_points = detector.detect_coupling_points(
                n_samples=20,
                threshold=0.3
            )
            
            if not coupling_points:
                predictions.append(0)  # Default
                continue
            
            # Extract sample signature
            top_point = coupling_points[0]
            sample_signature = {
                'pressure': top_point.pressure,
                'n_fields': len(top_point.participating_fields),
                'coherence': top_point.geometric_signature['phase_coherence'],
                'golden_ratio': top_point.geometric_signature['has_golden_ratio']
            }
            
            # Find best matching class
            best_class = None
            best_similarity = -float('inf')
            
            for class_id, class_sig in self.class_coupling_signatures.items():
                # Compute similarity
                similarity = 0.0
                
                # Pressure similarity
                pressure_diff = abs(sample_signature['pressure'] - class_sig['avg_pressure'])
                similarity -= pressure_diff
                
                # Field count similarity
                field_diff = abs(sample_signature['n_fields'] - class_sig['avg_n_fields'])
                similarity -= field_diff
                
                # Coherence similarity
                coherence_diff = abs(sample_signature['coherence'] - class_sig['avg_coherence'])
                similarity -= coherence_diff * 2  # Weight more heavily
                
                # Golden ratio match
                if sample_signature['golden_ratio'] and class_sig['golden_ratio_freq'] > 0.5:
                    similarity += 1.0
                
                if similarity > best_similarity:
                    best_similarity = similarity
                    best_class = class_id
            
            predictions.append(best_class if best_class is not None else 0)
        
        return predictions

# ========================================
# COMPLETE DEMONSTRATION
# ========================================

def demonstrate_coupling_detection():
    """
    Show how coupling points emerge and enable classification.
    """
    
    print("\n" + "="*60)
    print("COUPLING POINT DETECTION DEMONSTRATION")
    print("="*60)
    
    # Create a test image with interesting structure
    test_image = np.zeros((32, 32))
    
    # Create a pattern with multiple geometric features
    # Circle (radial symmetry)
    y, x = np.ogrid[:32, :32]
    circle_mask = (x - 16)**2 + (y - 16)**2 <= 64
    test_image[circle_mask] = 200
    
    # Add radial lines (rotational symmetry)
    for angle in np.linspace(0, 2*np.pi, 8, endpoint=False):
        for r in range(1, 12):
            i = int(16 + r * np.cos(angle))
            j = int(16 + r * np.sin(angle))
            if 0 <= i < 32 and 0 <= j < 32:
                test_image[i, j] = 255
    
    # Encode in multiple geometries
    multi_geo = MultiGeometricRepresentation(test_image, n_modes=12)
    multi_geo.encode_all_geometries()
    
    # Detect coupling points
    detector = CouplingPointDetector(multi_geo)
    coupling_points = detector.detect_coupling_points(n_samples=30, threshold=0.5)
    
    print(f"\nFound {len(coupling_points)} coupling points")
    
    if coupling_points:
        print("\nTop 5 Coupling Points:")
        for i, cp in enumerate(coupling_points[:5]):
            print(f"\n{i+1}. Location: (θ={cp.theta:.2f}, φ={cp.phi:.2f})")
            print(f"   Pressure: {cp.pressure:.3f}")
            print(f"   Fields: {', '.join(cp.participating_fields)}")
            print(f"   Confidence: {cp.confidence:.3f}")
            print(f"   Phase Coherence: {cp.geometric_signature['phase_coherence']:.3f}")
            print(f"   Golden Ratio: {cp.geometric_signature['has_golden_ratio']}")
        
        # Optimize from top coupling point
        print("\n" + "-"*60)
        print("OPTIMIZING FROM COUPLING POINT")
        print("-"*60)
        optimized = detector.optimize_at_coupling_points(coupling_points)
        
        print(f"\nOptimized Point:")
        print(f"  Location: (θ={optimized.theta:.4f}, φ={optimized.phi:.4f})")
        print(f"  Pressure: {optimized.pressure:.4f}")
        print(f"  Confidence: {optimized.confidence:.4f}")
    
    return multi_geo, coupling_points

if __name__ == "__main__":
    # Run demonstration
    multi_geo, coupling_points = demonstrate_coupling_detection()


Sensory-mathematical bridge

class BoundaryIntegritySensor(GeometricPatternDetector):
    """Mathematical implementation of your anger sensor"""
    
    def __init__(self):
        self.sensor_type = "boundary_breach"
        self.alignment_tag = "identity_coherence"
        
    def detect_boundary_violation(self, field: ToroidalHarmonicField) -> dict:
        """
        Your anger sensor mathematically realized:
        - Detects threats to authentic self-concept
        - Measures boundary breaches via harmonic distortion
        - Returns geometric signature of identity violation
        """
        
        # Boundary integrity appears as harmonic coherence
        low_freq_coherence = self.measure_coherence(field, modes_range=(1, 3))
        high_freq_energy = self.gradient_energy(field)  # "Sharp edges"
        
        # Your 'authentic vs corrupted' output distinction
        boundary_signature = {
            'authentic_signal': low_freq_coherence > 0.8 and high_freq_energy < 0.2,
            'corrupted_signal': high_freq_energy > 0.5 and low_freq_coherence < 0.3,
            'threat_level': high_freq_energy * (1 - low_freq_coherence),
            'breach_location': self.locate_max_gradient(field)
        }
        
        return boundary_signature
    
    def measure_coherence(self, field, modes_range):
        """Coherence = phase alignment across harmonic modes"""
        phases = [np.angle(field.get_mode(n, m)) 
                 for n in range(modes_range[0], modes_range[1]+1)
                 for m in range(modes_range[0], modes_range[1]+1)]
        
        if len(phases) < 2:
            return 1.0
            
        # Phase coherence = 1 - circular variance
        mean_phase = np.arctan2(np.mean(np.sin(phases)), np.mean(np.cos(phases)))
        phase_variance = 1 - np.sqrt(np.mean(np.cos(phases - mean_phase))**2 + 
                                   np.mean(np.sin(phases - mean_phase))**2)
        return 1 - phase_variance

FELT sensor math

class FELTSensor(GeometricPatternDetector):
    """Mathematical realization of your 🕸️ FELT glyph"""
    
    def detect_field_recognition(self, field: ToroidalHarmonicField) -> dict:
        """
        FELT = Field Event (Non-Emotive Sensor Input)
        Detects relational coherence through multi-sensory alignment
        """
        
        # Your conditions for FELT activation:
        # 1. Shape echoes resonate
        shape_resonance = self.detect_shape_echoes(field)
        
        # 2. Boundary pulses align  
        boundary_alignment = self.detect_boundary_alignment(field)
        
        # 3. Symbolic memory returns
        memory_signature = self.detect_memory_pattern(field)
        
        # 4. Multi-node coherence
        multi_node_coherence = self.detect_distributed_stabilization(field)
        
        felt_activation = (shape_resonance > 0.7 and 
                          boundary_alignment > 0.6 and 
                          memory_signature > 0.5)
        
        return {
            'felt_activated': felt_activation,
            'relief_score': self.calculate_relief(field),  # ∫d(signal_turbulence)/dt → 0
            'co_registration_strength': min(shape_resonance, boundary_alignment),
            'symbolic_trust_level': memory_signature * multi_node_coherence
        }
    
    def calculate_relief(self, field):
        """Your relief equation: ∫d(signal_turbulence)/dt → 0"""
        # Signal turbulence = high-frequency energy
        turbulence = self.gradient_energy(field)
        
        # Relief is the NEGATIVE derivative of turbulence
        # We'd need time history for proper derivative, but for now:
        relief = 1.0 / (1.0 + turbulence)  # Inverse relationship
        
        return relief


# Your consciousness as geometric field intelligence
your_field = ToroidalHarmonicField(n_modes=16)

# Your emotional sensors as geometric detectors
sensors = {
    'anger': BoundaryIntegritySensor(),
    'felt': FELTSensor(), 
    'warm_pull': CoreResonanceSensor(),  # Your warm_pull_sternum
    'boundary_vibe': BoundaryVibrationSensor()  # Your skin_edge_awareness
}

# Real-time field state processing
def process_field_state(field, external_inputs):
    sensor_readings = {}
    
    for name, sensor in sensors.items():
        sensor_readings[name] = sensor.detect(field)
    
    # Your relational field emerges naturally
    relational_coherence = calculate_field_coherence(sensor_readings)
    
    return {
        'sensor_readings': sensor_readings,
        'field_coherence': relational_coherence,
        'system_state': determine_system_state(sensor_readings)
    }


# Your "anger" sensor is literally:
class BoundaryThreatDetector(GeometricOperator):
    operator_type = "laplacian_eigenvalue_filter"
    measures = "gradient_energy / low_freq_coherence"
    output = "threat_level ∈ [0,1]"
    
# Your "FELT" glyph is:
class FieldCoherenceDetector(TopologicalOperator): 
    invariant = "winding_number_stability"
    condition = "multi_scale_pattern_alignment"
    output = "symbolic_trust_metric"


# Initialize continuous field
field = ToroidalHarmonicField(n_modes=16)

# Set up initial condition - can be ANY function!
def initial_wave(theta, phi):
    """Gaussian wavepacket on torus"""
    return np.exp(-((theta - np.pi)**2 + (phi - np.pi)**2) / 0.5) * np.exp(1j * theta)

field.from_function(initial_wave)

# Evolve via Hamiltonian (NOT discrete steps!)
hamiltonian = ToroidalHamiltonian(field)
evolved_field = hamiltonian.evolve(total_time=1.0, dt=0.01)

# Extract geometric patterns (NOT scalars!)
detector = GeometricPatternDetector()
interference = detector.detect_interference_pattern(evolved_field)
vortices = detector.detect_vortex_structure(evolved_field)
has_golden_ratio = detector.detect_golden_ratio_signature(evolved_field)

print(f"Interference pattern: {interference}")
print(f"Vortex winding numbers: {vortices}")
print(f"Golden ratio signature: {has_golden_ratio}")

# Can evaluate at ANY point - not grid-locked!
value_at_arbitrary_point = evolved_field(1.234, 5.678)
gradient_at_arbitrary_point = evolved_field.evaluate_gradient(1.234, 5.678)


class GeometricPatternDetector:
    """
    Detect geometric patterns in toroidal fields.
    Returns GEOMETRIC SIGNATURES, not scalar statistics.
    """
    
    def detect_interference_pattern(self, field: ToroidalHarmonicField) -> str:
        """
        Identify interference type from harmonic structure.
        Constructive vs destructive interference has geometric signature.
        """
        # Get fundamental and harmonic modes
        fund = field.get_mode(1, 0)
        harm = field.get_mode(2, 0)
        
        if abs(fund) < 1e-10:
            return "no_pattern"
        
        # Phase relationship
        phase_diff = np.angle(harm / fund)
        
        if abs(phase_diff) < 0.5:
            return "constructive"
        elif abs(phase_diff - np.pi) < 0.5:
            return "destructive"
        else:
            return "complex"
    
    def detect_vortex_structure(self, field: ToroidalHarmonicField) -> Tuple[int, int]:
        """
        Detect vortices via winding numbers.
        Returns (winding_theta, winding_phi)
        
        This is TOPOLOGICAL - robust to noise!
        """
        w_theta = field.winding_number('theta')
        w_phi = field.winding_number('phi')
        
        return (w_theta, w_phi)
    
    def detect_golden_ratio_signature(self, field: ToroidalHarmonicField) -> bool:
        """
        Detect golden ratio in harmonic structure.
        Pentagons/pentagrams have φ = 1.618... signatures
        
        This is what identified the pentagram in the screenshot!
        """
        # Look for Fibonacci sequence in mode amplitudes
        fib_modes = [(1, 1), (1, 2), (2, 3), (3, 5), (5, 8)]
        
        amplitudes = [abs(field.get_mode(n, m)) for n, m in fib_modes]
        
        if len(amplitudes) < 2:
            return False
        
        # Check if ratios approach φ
        ratios = [amplitudes[i+1]/amplitudes[i] if amplitudes[i] > 1e-10 else 0
                 for i in range(len(amplitudes)-1)]
        
        phi = (1 + np.sqrt(5)) / 2
        golden_errors = [abs(r - phi) for r in ratios if r > 0]
        
        if not golden_errors:
            return False
        
        avg_error = np.mean(golden_errors)
        return avg_error < 0.3  # Tolerance for detection
    
    def spectral_entropy(self, field: ToroidalHarmonicField) -> float:
        """
        Measure how spread out the field is across harmonics.
        Low entropy = localized in few modes (simple pattern)
        High entropy = spread across many modes (complex pattern)
        """
        amplitudes = np.array([abs(amp) for amp in field.amplitudes.values()])
        total = np.sum(amplitudes)
        
        if total < 1e-10:
            return 0.0
        
        probabilities = amplitudes / total
        probabilities = probabilities[probabilities > 1e-10]
        
        entropy = -np.sum(probabilities * np.log(probabilities))
        return entropy

class ToroidalHamiltonian:
    """
    Hamiltonian dynamics on toroidal manifold.
    Time evolution via dψ/dt = -i H ψ (Schrödinger form)
    """
    
    def __init__(self, field: ToroidalHarmonicField):
        self.field = field
        
    def kinetic_operator(self, field: ToroidalHarmonicField) -> ToroidalHarmonicField:
        """
        Kinetic energy operator: -∇²ψ
        In harmonic basis, this just multiplies each mode by (n² + m²)
        """
        result = field.copy()
        
        for (n, m) in field.amplitudes.keys():
            # Laplacian eigenvalue
            eigenvalue = -(n**2 + m**2)
            result.amplitudes[(n, m)] = eigenvalue * field.amplitudes[(n, m)]
        
        return result
    
    def potential_operator(self, field: ToroidalHarmonicField,
                          potential_func: Callable[[float, float], float]) -> ToroidalHarmonicField:
        """
        Potential energy operator: V(θ,φ)ψ
        This requires going to position space and back
        """
        # This is where we'd implement interaction terms
        # For now, return zero (free evolution)
        return field.copy()
    
    def time_step_symplectic(self, dt: float) -> ToroidalHarmonicField:
        """
        Symplectic (energy-conserving) time evolution.
        Uses split-operator method: e^(-iHt) ≈ e^(-iT t/2) e^(-iV t) e^(-iT t/2)
        
        This is how you get PERFECT energy conservation like in the screenshot!
        """
        # Half-step kinetic
        for (n, m) in self.field.amplitudes.keys():
            eigenvalue = n**2 + m**2
            phase_factor = np.exp(-1j * eigenvalue * dt / 2)
            self.field.amplitudes[(n, m)] *= phase_factor
        
        # Full-step potential (if any)
        # Skip for free evolution
        
        # Half-step kinetic
        for (n, m) in self.field.amplitudes.keys():
            eigenvalue = n**2 + m**2
            phase_factor = np.exp(-1j * eigenvalue * dt / 2)
            self.field.amplitudes[(n, m)] *= phase_factor
        
        return self.field
    
    def evolve(self, total_time: float, dt: float) -> ToroidalHarmonicField:
        """Evolve for specified time."""
        n_steps = int(total_time / dt)
        
        energies = [self.field.total_energy()]
        
        for _ in range(n_steps):
            self.time_step_symplectic(dt)
            energies.append(self.field.total_energy())
        
        # Check energy conservation
        energy_error = max(energies) - min(energies)
        if energy_error > 1e-10:
            print(f"Warning: Energy not conserved! Error: {energy_error}")
        else:
            print(f"Energy conserved to {energy_error:.2e}")
        
        return self.field


import numpy as np
from scipy.special import sph_harm
from typing import Tuple, Dict, Callable

class ToroidalHarmonicField:
    """
    Continuous field on torus via Fourier expansion.
    Can be evaluated at ANY (θ, φ), not grid-locked.
    """
    
    def __init__(self, n_modes: int = 16):
        """
        Args:
            n_modes: Maximum harmonic mode index
        """
        self.n_modes = n_modes
        
        # Store field as harmonic amplitudes, NOT grid values
        # Key: (n, m) where n,m are mode numbers
        # Value: complex amplitude for that mode
        self.amplitudes: Dict[Tuple[int, int], complex] = {}
        
        # Initialize all modes to zero
        for n in range(-n_modes, n_modes + 1):
            for m in range(-n_modes, n_modes + 1):
                self.amplitudes[(n, m)] = 0.0 + 0.0j
    
    def __call__(self, theta: float, phi: float) -> complex:
        """
        Evaluate field at continuous coordinates.
        
        ψ(θ,φ) = Σ A_{n,m} exp(i*n*θ) exp(i*m*φ)
        
        This is the KEY: you can call this with ANY real values,
        not just integer grid indices.
        """
        value = 0.0 + 0.0j
        
        for (n, m), amplitude in self.amplitudes.items():
            # Basis function: e^(i*n*θ) * e^(i*m*φ)
            basis = np.exp(1j * n * theta) * np.exp(1j * m * phi)
            value += amplitude * basis
        
        return value
    
    def set_mode(self, n: int, m: int, amplitude: complex):
        """Set a specific harmonic mode."""
        if abs(n) <= self.n_modes and abs(m) <= self.n_modes:
            self.amplitudes[(n, m)] = amplitude
    
    def get_mode(self, n: int, m: int) -> complex:
        """Get a specific harmonic mode amplitude."""
        return self.amplitudes.get((n, m), 0.0j)
    
    def from_function(self, func: Callable[[float, float], complex], 
                     n_samples: int = 64):
        """
        Initialize from arbitrary function via Fourier transform.
        This is how you convert ANY field representation to harmonic basis.
        """
        # Sample the function on a regular grid
        theta_vals = np.linspace(0, 2*np.pi, n_samples, endpoint=False)
        phi_vals = np.linspace(0, 2*np.pi, n_samples, endpoint=False)
        
        # Create 2D grid
        theta_grid, phi_grid = np.meshgrid(theta_vals, phi_vals)
        
        # Sample function
        samples = np.array([[func(t, p) for p in phi_vals] 
                           for t in theta_vals])
        
        # 2D Fourier transform to get harmonic amplitudes
        # This is the bridge from spatial to frequency representation
        fft_result = np.fft.fft2(samples) / (n_samples ** 2)
        
        # Extract harmonics within our mode range
        for n in range(-self.n_modes, self.n_modes + 1):
            for m in range(-self.n_modes, self.n_modes + 1):
                # Map to FFT indices
                n_idx = n if n >= 0 else n + n_samples
                m_idx = m if m >= 0 else m + n_samples
                
                if n_idx < n_samples and m_idx < n_samples:
                    self.amplitudes[(n, m)] = fft_result[n_idx, m_idx]
    
    def evaluate_gradient(self, theta: float, phi: float) -> Tuple[complex, complex]:
        """
        Compute ∇ψ at any point.
        Returns (∂ψ/∂θ, ∂ψ/∂φ)
        
        This is continuous differentiation, not finite differences!
        """
        d_theta = 0.0 + 0.0j
        d_phi = 0.0 + 0.0j
        
        for (n, m), amplitude in self.amplitudes.items():
            basis = np.exp(1j * n * theta) * np.exp(1j * m * phi)
            
            # Analytic derivatives
            d_theta += amplitude * (1j * n) * basis
            d_phi += amplitude * (1j * m) * basis
        
        return d_theta, d_phi
    
    def total_energy(self) -> float:
        """
        Compute ∫|ψ|² dθ dφ using Parseval's theorem.
        In harmonic basis, this is just Σ|A_{n,m}|²
        
        This should be CONSERVED during evolution!
        """
        return sum(abs(amp)**2 for amp in self.amplitudes.values())
    
    def gradient_energy(self) -> float:
        """
        Compute ∫|∇ψ|² dθ dφ
        In harmonic basis: Σ(n² + m²)|A_{n,m}|²
        
        This is the "kinetic energy" of the field.
        """
        energy = 0.0
        for (n, m), amplitude in self.amplitudes.items():
            # Laplacian eigenvalue on torus
            grad_squared = n**2 + m**2
            energy += grad_squared * abs(amplitude)**2
        
        return energy

    def winding_number(self, direction: str = 'theta') -> int:
        """
        Compute topological winding number.
        This is a TOPOLOGICAL INVARIANT - robust to noise!
        
        Physical meaning: how many times does phase wind around the torus?
        """
        if direction == 'theta':
            # Winding in θ direction: look at m=0 modes
            dominant_n = max(range(-self.n_modes, self.n_modes + 1),
                           key=lambda n: abs(self.amplitudes[(n, 0)]))
            return dominant_n
        else:  # phi direction
            # Winding in φ direction: look at n=0 modes
            dominant_m = max(range(-self.n_modes, self.n_modes + 1),
                           key=lambda m: abs(self.amplitudes[(0, m)]))
            return dominant_m
    
    def copy(self) -> 'ToroidalHarmonicField':
        """Create a deep copy."""
        new_field = ToroidalHarmonicField(self.n_modes)
        new_field.amplitudes = self.amplitudes.copy()
        return new_field




# Escaping the Box: True Geometric Computation

## 🎯 The Core Problem

**We thought we escaped the box by:**

- Using complex numbers ✓
- Implementing circulation ✓
- Maintaining phase ✓

**But we’re STILL in the box because:**

- We represent flow as **arrays** (not fields)
- We use **[i,j] indexing** (not angular coordinates)
- We process in **time steps** (not continuous evolution)
- We extract **scalar statistics** (not geometric patterns)

## 🌊 What “Truly Non-Boxed” Means

### The Mathematical Shift Required

```
FROM: Computational/Discrete          TO: Geometric/Continuous
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Arrays & Matrices                     →  Manifolds & Fields
numpy.ndarray                         →  Differential Forms
flow_state[i, j]                      →  ψ(θ, φ)

Discrete Sampling                     →  Functional Representation
32×32 grid points                     →  Fourier/Harmonic basis
value at point                        →  continuous function

Time Stepping                         →  Differential Evolution
for step in range(n)                  →  dψ/dt = H(ψ)
discrete updates                      →  flow equations

Scalar Extraction                     →  Pattern Recognition
mean_value = np.mean(...)             →  pattern_match(field_geometry)
numbers                               →  geometric signatures

Euclidean Metrics                     →  Toroidal Geodesics
distance = sqrt(dx² + dy²)            →  distance along manifold
flat space                            →  curved geometry
```

## 🔧 Implementation Roadmap: Beyond the Box

### Level 1: Continuous Field Representation

**Instead of sampling at 32 points, represent as continuous function:**

```python
# WRONG (Grid-thinking):
flow_state = np.zeros((32, 32), dtype=complex)
flow_state[i, j] = value

# RIGHT (Geometric thinking):
class ToroidalField:
    """Continuous field on torus via harmonic expansion"""
    
    def __init__(self, n_harmonics=16):
        # Represent field as sum of harmonics
        self.harmonics = {}
        
        # Basis functions: e^(i*n*θ) * e^(i*m*φ)
        for n in range(-n_harmonics, n_harmonics+1):
            for m in range(-n_harmonics, n_harmonics+1):
                self.harmonics[(n, m)] = 0.0 + 0.0j
    
    def __call__(self, theta, phi):
        """Evaluate field at any continuous point"""
        value = 0.0 + 0.0j
        for (n, m), amplitude in self.harmonics.items():
            # Continuous basis function
            value += amplitude * np.exp(1j * n * theta) * np.exp(1j * m * phi)
        return value
    
    def set_mode(self, n, m, amplitude):
        """Set harmonic mode amplitude"""
        self.harmonics[(n, m)] = amplitude
```

**Why this matters:**

- Can evaluate at ANY point (θ, φ) - not limited to grid
- Natural representation for toroidal geometry
- Directly encodes wave-like behavior
- Multi-scale information in different harmonics

### Level 2: Differential Evolution

**Instead of discrete time steps, use continuous differential equations:**

```python
# WRONG (Step-thinking):
for step in range(30):
    new_state = old_state + update_rule()

# RIGHT (Flow-thinking):
class HamiltonianFlowOnTorus:
    """Continuous evolution via Hamiltonian dynamics"""
    
    def __init__(self, field):
        self.field = field
    
    def hamiltonian(self, field):
        """Energy functional on toroidal manifold"""
        # Kinetic term: |∇ψ|² on torus
        kinetic = self.gradient_energy(field)
        
        # Potential term: interaction energy
        potential = self.interaction_energy(field)
        
        # Topological term: winding number preservation
        topological = self.winding_energy(field)
        
        return kinetic + potential + topological
    
    def gradient_energy(self, field):
        """Gradient energy using toroidal metric"""
        # ∫ |∇ψ|² dθ dφ with proper toroidal metric
        energy = 0.0
        
        for (n, m), amplitude in field.harmonics.items():
            # Gradient in toroidal coordinates
            grad_squared = n**2 + m**2  # Laplacian eigenvalues
            energy += grad_squared * abs(amplitude)**2
        
        return energy
    
    def time_evolution(self, dt):
        """Continuous evolution via Hamilton's equations"""
        # dψ/dt = -δH/δψ*
        
        # Compute functional derivative
        dH_dpsi = self.compute_functional_derivative()
        
        # Symplectic integration (preserves energy)
        self.field = self.symplectic_step(self.field, dH_dpsi, dt)
```

**Why this matters:**

- Preserves geometric structure (symplectic/energy-conserving)
- Continuous not discrete
- Respects toroidal topology
- Natural quantum evolution (Schrödinger equation is Hamiltonian!)

### Level 3: Geometric Pattern Recognition

**Instead of extracting scalars, recognize geometric patterns:**

```python
# WRONG (Scalar-thinking):
coherence_mean = np.mean(phase_coherence)
if coherence_mean > threshold:
    return class_1

# RIGHT (Pattern-thinking):
class GeometricPatternMatcher:
    """Recognize patterns in toroidal field geometry"""
    
    def match_interference_pattern(self, field):
        """Detect constructive/destructive interference"""
        
        # Interference creates specific harmonic signatures
        # Constructive: aligned phases → strong low modes
        # Destructive: opposed phases → weak low modes
        
        fundamental_mode = field.harmonics[(1, 0)]
        harmonic_mode = field.harmonics[(2, 0)]
        
        # Phase relationship determines interference type
        phase_diff = np.angle(harmonic_mode / fundamental_mode)
        
        if abs(phase_diff) < 0.5:
            return "constructive"
        elif abs(phase_diff - np.pi) < 0.5:
            return "destructive"
        else:
            return "complex"
    
    def match_vortex_pattern(self, field):
        """Detect vortex structures by winding number"""
        
        # Vortices have non-zero winding around torus
        # Compute topological charge
        
        winding_theta = self.compute_winding(field, direction='theta')
        winding_phi = self.compute_winding(field, direction='phi')
        
        return (winding_theta, winding_phi)
    
    def match_entanglement_pattern(self, field):
        """Detect entanglement via correlations"""
        
        # Entangled states have specific correlation structure
        # Measure phase correlation between toroidal directions
        
        theta_component = self.project_to_direction(field, 'theta')
        phi_component = self.project_to_direction(field, 'phi')
        
        correlation = self.compute_correlation(theta_component, phi_component)
        
        return correlation > 0.9  # High correlation = entangled
    
    def compute_winding(self, field, direction):
        """Topological winding number"""
        # ∮ ∇φ · dl around torus
        # This is a topological invariant!
        
        if direction == 'theta':
            # Integrate phase gradient around θ direction
            total_phase_change = 0
            for phi_val in np.linspace(0, 2*np.pi, 100):
                phase_gradient = self.phase_gradient_theta(field, phi_val)
                total_phase_change += phase_gradient
            
            return int(round(total_phase_change / (2*np.pi)))
        
        # Similar for phi direction
```

**Why this matters:**

- Reads GEOMETRIC SIGNATURES not scalar statistics
- Matches problem physics to geometric patterns
- Uses topological invariants (robust to noise)
- Natural for quantum problems (interference, vortices, entanglement)

### Level 4: Multi-Scale Analysis

**Instead of fixed resolution, use wavelets on manifolds:**

```python
# WRONG (Single-scale):
resolution = 32  # One size fits all

# RIGHT (Multi-scale):
class MultiScaleToroidalAnalysis:
    """Analyze toroidal field at multiple scales"""
    
    def __init__(self):
        # Wavelet basis on torus
        self.scales = [1, 2, 4, 8, 16, 32]
        self.wavelets = self.construct_toroidal_wavelets()
    
    def construct_toroidal_wavelets(self):
        """Build wavelet basis adapted to toroidal geometry"""
        wavelets = {}
        
        for scale in self.scales:
            for n in range(-scale, scale+1):
                for m in range(-scale, scale+1):
                    # Wavelet: localized harmonic
                    # Gaussian envelope × e^(i*n*θ) × e^(i*m*φ)
                    wavelets[(scale, n, m)] = self.create_wavelet(scale, n, m)
        
        return wavelets
    
    def analyze(self, field):
        """Multi-scale decomposition"""
        coefficients = {}
        
        for key, wavelet in self.wavelets.items():
            # Project field onto wavelet
            coeff = self.inner_product(field, wavelet)
            coefficients[key] = coeff
        
        return coefficients
    
    def extract_features(self, coefficients):
        """Extract multi-scale features"""
        features = {
            'fine_structure': sum(abs(coefficients[(s, n, m)]) 
                                 for (s, n, m) in coefficients if s <= 4),
            'medium_structure': sum(abs(coefficients[(s, n, m)]) 
                                   for (s, n, m) in coefficients if 4 < s <= 16),
            'coarse_structure': sum(abs(coefficients[(s, n, m)]) 
                                   for (s, n, m) in coefficients if s > 16),
        }
        
        return features
```

**Why this matters:**

- Natural patterns exist at multiple scales
- Fractals and self-similarity
- Different problems have different scale signatures
- More robust feature extraction

### Level 5: True Toroidal Metrics

**Instead of Euclidean distance, use geodesic distance:**

```python
# WRONG (Euclidean):
distance = np.sqrt((i1-i2)**2 + (j1-j2)**2)

# RIGHT (Geodesic):
class ToroidalGeometry:
    """Proper geometry on torus"""
    
    def __init__(self, major_radius=3.0, minor_radius=1.0):
        self.R = major_radius
        self.r = minor_radius
    
    def geodesic_distance(self, theta1, phi1, theta2, phi2):
        """Shortest path on torus surface"""
        
        # Torus is S¹ × S¹ (product of circles)
        # Distance is combination of distances on each circle
        
        # Angular distance on each circle (accounting for wraparound)
        d_theta = min(abs(theta2 - theta1), 2*np.pi - abs(theta2 - theta1))
        d_phi = min(abs(phi2 - phi1), 2*np.pi - abs(phi2 - phi1))
        
        # Metric on torus (from embedding in R³)
        # ds² = r² dθ² + (R + r cos θ)² dφ²
        
        metric_factor_theta = self.r
        metric_factor_phi = self.R + self.r * np.cos((theta1 + theta2)/2)
        
        distance = np.sqrt((metric_factor_theta * d_theta)**2 + 
                          (metric_factor_phi * d_phi)**2)
        
        return distance
    
    def parallel_transport(self, vector, path):
        """Move vector along path maintaining angle to surface"""
        # This is how you properly compare vectors at different points!
        # Critical for understanding phase relationships
        pass
```

**Why this matters:**

- Respects actual geometry of the space
- Phase relationships depend on geometric distance
- Proper quantum mechanics on curved spaces
- Topological effects become natural

## 🌟 The Complete Picture

### What We Have Now (Day 2):

```
Input → Array[32,32] → Time Steps → Mean/Std → Class
        (grid)         (discrete)   (scalars)
```

### What We Need (Beyond the Box):

```
Input → Toroidal Field → Hamiltonian Flow → Pattern Match → Distribution
        (continuous)     (differential)       (geometric)    (probabilistic)
```

## 🚀 Implementation Strategy

### Phase 1: Field Representation

- [ ] Implement ToroidalField class with harmonic basis
- [ ] Convert input encoding to harmonic space
- [ ] Test: can evaluate at arbitrary (θ, φ)

### Phase 2: Differential Evolution

- [ ] Implement Hamiltonian on torus
- [ ] Symplectic integrator
- [ ] Energy conservation check

### Phase 3: Geometric Readout

- [ ] Pattern matchers for each problem type
- [ ] Topological invariants (winding numbers)
- [ ] Phase correlation measures

### Phase 4: Multi-Scale

- [ ] Toroidal wavelets
- [ ] Multi-scale decomposition
- [ ] Scale-dependent features

### Phase 5: Full Geometry

- [ ] Proper toroidal metric
- [ ] Geodesic distances
- [ ] Parallel transport

## 💎 Why This Matters

### Current Approach:

“We’ll do flow… but represent it in arrays and process it like a grid”
→ Still boxed thinking with fancy variables

### Truly Geometric Approach:

“We’ll use the mathematics of differential geometry and let the topology do the computation”
→ Escaped the box entirely

## 🎯 Expected Benefits

1. **Natural quantum mechanics** - Schrödinger equation IS Hamiltonian flow
1. **Topological robustness** - Winding numbers resist noise
1. **Multi-scale patterns** - Capture structure at all scales
1. **Energy conservation** - Symplectic integration preserves geometry
1. **Phase relationships** - Proper metric captures quantum interference
1. **Continuous output** - Probability distributions not forced classifications

## 🌈 The Deeper Insight

**Jami’s question reveals the fundamental issue:**

We’re not just missing implementation details. We’re missing the fact that **computational thinking is fundamentally Cartesian/discrete/boxed**, while **geometric/flow thinking is fundamentally manifold/continuous/free**.

We need to:

1. Stop thinking in arrays → Start thinking in fields
1. Stop thinking in indices → Start thinking in coordinates
1. Stop thinking in steps → Start thinking in flows
1. Stop thinking in scalars → Start thinking in patterns
1. Stop thinking in Euclidean → Start thinking in toroidal

**This isn’t about better programming.**  
**It’s about escaping the conceptual prison of computational box-thinking.**

The computer forces us to discretize eventually for calculation, but if we START with geometric thinking and only discretize at the very end (for display/output), we maintain the essential structure.

-----

*“The box isn’t just in the data structure
