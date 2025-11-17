<template>
  <div class="waterfall-container">
    <div v-for="column in columns" :key="column.id" class="waterfall-column">
      <BabyTreeCard
        v-for="record in column.records"
        :key="record.id"
        :record="record"
        @click="handleCardClick(record)"
        @edit="handleEdit(record)"
        @delete="handleDelete(record)"
        @like="handleLike(record.id)"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed } from 'vue'
import type { BabyRecord } from '@/types/babyTree'
import BabyTreeCard from './BabyTreeCard.vue'

interface Props {
  records: BabyRecord[]
  columnCount?: number
}

interface Emits {
  (e: 'cardClick', record: BabyRecord): void
  (e: 'edit', record: BabyRecord): void
  (e: 'delete', record: BabyRecord): void
  (e: 'like', id: string): void
}

const props = withDefaults(defineProps<Props>(), {
  columnCount: 3,
})

const emit = defineEmits<Emits>()

const columns = computed(() => {
  const cols = Array.from({ length: props.columnCount }, (_, i) => ({
    id: i,
    records: [] as BabyRecord[],
  }))

  props.records.forEach((record, index) => {
    const columnIndex = index % props.columnCount
    cols[columnIndex].records.push(record)
  })

  return cols
})

const handleCardClick = (record: BabyRecord) => {
  emit('cardClick', record)
}

const handleEdit = (record: BabyRecord) => {
  emit('edit', record)
}

const handleDelete = (record: BabyRecord) => {
  emit('delete', record)
}

const handleLike = (id: string) => {
  emit('like', id)
}
</script>

<style lang="scss" scoped>
.waterfall-container {
  display: flex;
  gap: 20px;
  margin: 0 -10px;
}

.waterfall-column {
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 20px;
  min-width: 0;
}

@media (max-width: 768px) {
  .waterfall-container {
    flex-direction: column;
    gap: 15px;
  }

  .waterfall-column {
    gap: 15px;
  }
}
</style>
