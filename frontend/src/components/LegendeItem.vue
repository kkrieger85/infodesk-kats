<template>
  <div class="legende">
    <i>
      <slot name="icon"></slot>
    </i>
    <p class="details">
      <slot name="explanation"></slot>
      <slot></slot>
    </p>
  </div>
</template>

<style scoped>
.legende {
  display: flex;
  position: relative;
  padding: 1rem;
  border-top: 1px dotted #000;
}

.details {
  flex: 1;
  margin-left: 1rem;
}

i {
  display: flex;
  place-items: center;
  place-content: center;
  width: 32px;
  height: 32px;

  color: var(--color-text);
}

h3 {
  font-size: 1.2rem;
  font-weight: 500;
  margin-bottom: 0.4rem;
  color: var(--color-heading);
}

@media (max-width: 800px) {}

@media (min-width: 1024px) {
  .legende {
    margin-left: 25px;
    margin-top: 0;
    padding: 0.4rem 0 1rem 1.5rem;
  }

  i {
    left: -16px;
    position: absolute;
    background: var(--color-background);
    border-radius: 8px;
  }

  .legende:before {
    content: ' ';
    border-left: 1px solid var(--color-border);
    position: absolute;
    left: 0;
    bottom: calc(50% + 25px);
    height: calc(50% - 25px);
  }

  .legende:after {
    content: ' ';
    border-left: 1px solid var(--color-border);
    position: absolute;
    left: 0;
    top: calc(50% + 25px);
    height: calc(50% - 25px);
  }

  .legende:first-of-type:before {
    display: none;
  }

  .legende:last-of-type:after {
    display: none;
  }
}
</style>
