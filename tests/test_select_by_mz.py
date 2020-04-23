from matchms import Spectrum
from matchms.filtering import select_by_mz
import numpy


def test_select_by_mz_no_parameters_1():

    mz = numpy.array([10, 20, 30, 40], dtype="float")
    intensities = numpy.array([1, 10, 100, 1000], dtype="float")
    spectrum_in = Spectrum(mz=mz, intensities=intensities, metadata=dict())

    spectrum = select_by_mz(spectrum_in)

    assert spectrum.mz.size == 4
    assert spectrum.mz.size == spectrum.intensities.size
    assert numpy.array_equal(spectrum.mz, numpy.array([10, 20, 30, 40], dtype="float"))
    assert numpy.array_equal(spectrum.intensities, numpy.array([1, 10, 100, 1000], dtype="float"))


def test_select_by_mz_no_parameters_2():

    mz = numpy.array([998, 999, 1000, 1001, 1002], dtype="float")
    intensities = numpy.array([1, 10, 100, 1000, 10000], dtype="float")
    spectrum_in = Spectrum(mz=mz, intensities=intensities)

    spectrum = select_by_mz(spectrum_in)

    assert spectrum.mz.size == 3
    assert spectrum.mz.size == spectrum.intensities.size
    assert numpy.array_equal(spectrum.mz, numpy.array([998, 999, 1000], dtype="float"))
    assert numpy.array_equal(spectrum.intensities, numpy.array([1, 10, 100], dtype="float"))


def test_select_by_mz_with_from_parameter():

    mz = numpy.array([10, 20, 30, 40], dtype="float")
    intensities = numpy.array([1, 10, 100, 1000], dtype="float")
    spectrum_in = Spectrum(mz=mz, intensities=intensities)

    spectrum = select_by_mz(spectrum_in, mz_from=15.0)

    assert spectrum.mz.size == 3
    assert spectrum.mz.size == spectrum.intensities.size
    assert numpy.array_equal(spectrum.mz, numpy.array([20, 30, 40], dtype="float"))
    assert numpy.array_equal(spectrum.intensities, numpy.array([10, 100, 1000], dtype="float"))


def test_select_by_mz_with_to_parameter():

    mz = numpy.array([10, 20, 30, 40], dtype="float")
    intensities = numpy.array([1, 10, 100, 1000], dtype="float")
    spectrum_in = Spectrum(mz=mz, intensities=intensities)

    spectrum = select_by_mz(spectrum_in, mz_to=35.0)

    assert spectrum.mz.size == 3
    assert spectrum.mz.size == spectrum.intensities.size
    assert numpy.array_equal(spectrum.mz, numpy.array([10, 20, 30], dtype="float"))
    assert numpy.array_equal(spectrum.intensities, numpy.array([1, 10, 100], dtype="float"))


def test_select_by_mz_with_from_and_to_parameters():

    mz = numpy.array([10, 20, 30, 40], dtype="float")
    intensities = numpy.array([1, 10, 100, 1000], dtype="float")
    spectrum_in = Spectrum(mz=mz, intensities=intensities)

    spectrum = select_by_mz(spectrum_in, mz_from=15.0, mz_to=35.0)

    assert spectrum.mz.size == 2
    assert spectrum.mz.size == spectrum.intensities.size
    assert numpy.array_equal(spectrum.mz, numpy.array([20, 30], dtype="float"))
    assert numpy.array_equal(spectrum.intensities, numpy.array([10, 100], dtype="float"))
