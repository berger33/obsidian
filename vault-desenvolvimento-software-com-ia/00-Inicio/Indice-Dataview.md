---
tipo: moc
dominio: fundamentos
nivel: iniciante
confianca: alta
ultima_verificacao: 2026-09-30
validade: estavel
fontes: []
tags: [indice, dataview]
aliases: [Índice dinâmico]
---
# Índice Dinâmico Dataview

```dataview
TABLE tipo, dominio, nivel, confianca, validade
FROM ""
WHERE tipo
SORT dominio ASC, tipo ASC, file.name ASC
```

## Por domínio
```dataview
TABLE rows.file.link AS Notas
FROM ""
WHERE dominio
GROUP BY dominio
```
