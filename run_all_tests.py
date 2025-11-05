#!/usr/bin/env python3
"""
Run all tests in the python_kactl library
"""

import sys
import os
import subprocess
import time

def run_test(test_file):
    """Run a single test file and return result"""
    print(f"Running {test_file}...", end=" ")
    start = time.time()
    
    try:
        result = subprocess.run(
            [sys.executable, test_file],
            cwd=os.path.dirname(os.path.abspath(__file__)),
            capture_output=True,
            text=True,
            timeout=30
        )
        elapsed = time.time() - start
        
        if result.returncode == 0:
            print(f"✅ PASSED ({elapsed:.2f}s)")
            return True, None
        else:
            print(f"❌ FAILED ({elapsed:.2f}s)")
            return False, result.stderr or result.stdout
    except subprocess.TimeoutExpired:
        print(f"❌ TIMEOUT (>30s)")
        return False, "Test timed out after 30 seconds"
    except Exception as e:
        print(f"❌ ERROR")
        return False, str(e)

def main():
    """Run all tests"""
    test_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'tests')
    
    if not os.path.exists(test_dir):
        print(f"❌ Test directory not found: {test_dir}")
        return 1
    
    # Find all test files
    test_files = []
    for file in os.listdir(test_dir):
        if file.startswith('test_') and file.endswith('.py'):
            test_files.append(os.path.join(test_dir, file))
    
    test_files.sort()
    
    if not test_files:
        print("No test files found!")
        return 1
    
    print(f"\n{'='*60}")
    print(f"Running {len(test_files)} test files")
    print(f"{'='*60}\n")
    
    passed = 0
    failed = 0
    errors = []
    
    for test_file in test_files:
        success, error = run_test(test_file)
        if success:
            passed += 1
        else:
            failed += 1
            errors.append((os.path.basename(test_file), error))
    
    # Print summary
    print(f"\n{'='*60}")
    print(f"TEST SUMMARY")
    print(f"{'='*60}")
    print(f"Total:  {len(test_files)}")
    print(f"Passed: {passed} ✅")
    print(f"Failed: {failed} ❌")
    print(f"{'='*60}\n")
    
    # Print errors
    if errors:
        print("FAILED TESTS:")
        print("-" * 60)
        for test_name, error in errors:
            print(f"\n{test_name}:")
            if error:
                print(error[:500])  # Print first 500 chars
        print("-" * 60)
        return 1
    else:
        print("🎉 ALL TESTS PASSED! 🎉\n")
        return 0

if __name__ == "__main__":
    sys.exit(main())
