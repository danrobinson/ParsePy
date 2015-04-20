import abc
import copy
from parse_rest.core import ParseError
from parse_rest.datatypes import Object

def encode(value):
	"""Encode a value in a way that can be understood by Parse."""
	pass

class Operation(object):
    __metaclass__ = abc.ABCMeta

	def _mergeWithPrevious(self, previous):
		return

	def _apply(self, oldValue):
		return

	def toJSON(self):
		return

class Set(Operation):
	"""Implements Parse's set' operation."""

	def __init__(self, value):
		self.value = value

	def _mergeWithPrevious(self, previous):
		return self

	def _apply(self, oldValue):
		return self.value

	def toJSON(self):
		return self.value

class Delete(Operation):

	def _mergeWithPrevious(self, previous):
		return self

	def _apply(self, oldValue):
		return None

	def toJSON(self):
    	return {"__op": "Delete"}

class Increment(Operation):

	def __init__(self, amount=1):
		self.amount = amount

    def _mergeWithPrevious(previous):
    	if not previous:
        	return self
      	elif isinstance(previous, Delete):
        	return Set(self.amount)
        elif isinstance(previous, Set):
        	return Set(previous.value + self.amount)
        elif isinstance(previous, Increment):
        	return Increment(self.amount + previous.amount)
        else:
        	raise ParseError("Cannot use Increment operation after previous operation.")
	
	def _apply(self, oldValue):
		return oldValue + amount

	def toJSON(self):
		return { "__op": "Increment", "amount": self.amount }

class Add(Operation):

	def __init__(self, objects):
		if not isinstance(objects, list):
			raise ParseError("The Add operation requires a list of objects to be added.")
		self.value = objects

	def _mergeWithPrevious(previous):
		if not previous:
			return self
		elif isinstance(previous, Delete):
			return Set(self.objects)
		elif isinstance(previous, Set):
			return Set(previous.value + self.objects)
		elif isinstance(previous, Add):
			return Add(previous.objects + self.objects)
		else:
			raise ParseError("Cannot use Add operation after previous operation.")

	def _apply(self, oldValue):
		if not oldValue:
			return copy.copy(self.objects)
		return oldValue + self.objects

    def toJSON: function() {
    	return { "__op": "Add", "objects": encode(self.objects)}

class AddUnique(Operation):

	__init__(self, objects):
		if not isinstance(objects, list):
			raise ParseError("The AddUnique operation requires a list of objects to be added.")
		self.objects = objects

	def _mergeWithPrevious(self, previous):
		if not previous:
			return self
		elif isinstance(previous, Delete):
			return Set(this.objects)
		elif isinstance(previous, Set):
			return Set(this._apply(previous.value))
		elif isinstance(previous, addUnique):
			return AddUnique(this._apply(previous.objects))

	def _apply(self, oldValue):
		if not oldValue:
			return copy.copy(self.objects)
		else:
			newValue = copy.copy(oldValue)
			for obj in self.objects:
				if instanceof(obj, Object) and obj in oldValue:
					"""COMPLETE LATER"""

	def toJSON(self):
		return {"__op": "AddUnique", "objects": encode(self.objects)}


class Remove(Operation):

	def __init__(self, objects):
		if not isinstance(objects, list):
			raise ParseError("The Remove operation requires a list of objects to be added.")
		self.objects = objects

	def _mergeWithPrevious(self, previous):
		if not previous:
			return self
		elif isinstance(previous, Delete):
			return previous
		elif isinstance(previous, Set):
			return Set(self._apply(previous.value, self.objects))
		elif isinstance(previous, Remove):
			return Remove(previous.objects + this.objects)
		else:
			raise ParseError("Cannot use Remove operation after previous operation")

	def _apply(oldObjects):
		if not oldObjects:
			return []
		newObjects = []
		for oldObj in oldObjects:
			for newObj in self.objects:
				if instanceof(oldObj, Object)
					if instanceof(newObj, Object) and not oldObj.isDirty() and oldObj.id == newObj.id:
						pass
					else:
						newObjects.append(oldObj)
				else:
					# Neither are objects
					if oldObj !== newObj:
						newObjects.append(oldObj)
		return newObjects

	def toJSON(self):
		return {"__op": "Remove", "objects": encode(self.objects)}

class RelationOperation(Operation):

	def __init__(self, adds, removes):
		self.targetClassName = None
		self.relations_to_add = 
		self.relations_to_remove = []
		if adds:
			self.check_and_assign_class_name(adds)
			self.add_objects(adds, self.relations_to_add)
		if removes:
			self.check_and_assign_class_name(removes)
			self.add_objects(removes, self.relations_to_remove)
		if not self.target_class_name:
			raise ParseError("Cannot create a ParseRelationOperation with no objects.")

	def check_and_assign_class_name(self, objects):
		for object in objects:
			if not self.target_class_name:
				self.target_class_name = object.get_class_name()
			if not object.id:
				raise ParseError("You can't add an unsaved Parse object to a relation.")
			if self.target_class_name is not object.get_class_name():
				raise ParseError("All objects in a relation must be of the same class.")

	def add_objects(objects, container):
		if not isinstance(objects, list):
			objects = [objects]
		for object in objects:
			if not object.id:
				container["None"].append(object)
			else:
				container[]









