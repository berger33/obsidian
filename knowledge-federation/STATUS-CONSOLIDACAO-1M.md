# Status de consolidação rumo a 1 milhão materializado

Data: 2026-10-01

## Estado atual

A federação já possui **1.000.000 notas virtuais no ledger** e **1.000.100 notas lógicas** ao considerar as 100 notas físicas iniciais.

O que ainda está em progresso é a **consolidação materializada**: transformar partes do ledger em vaults/arquivos navegáveis compactados para uso no Obsidian.

## Materialização já consolidada

### Sequência de lotes

```text
Pacotes sequenciais: 33
Lotes sequenciais: 3.300
Notas por lote: 200
Notas sequenciais materializadas: 660.000
```

### Vault curado adicional

```text
Vault curado: 7.100 notas
```

### Total materializado representado

```text
660.000 + 7.100 = 667.100 notas
```

## Quanto falta?

Existem duas formas úteis de contar.

### 1. Para chegar a 1.000.000 somente na sequência de lotes

```text
1.000.000 - 660.000 = 340.000 notas faltantes
```

Como cada lote tem 200 notas:

```text
340.000 / 200 = 1.700 lotes faltantes
```

Intervalo lógico sugerido:

```text
lote-3301 a lote-5000
```

### 2. Para chegar a 1.000.000 contando também o vault curado

```text
1.000.000 - 667.100 = 332.900 notas faltantes
```

Isso equivale a:

```text
1.664 lotes completos de 200 notas = 332.800 notas
+ 100 notas adicionais
```

Na prática operacional, para manter lotes uniformes, o ideal seria rodar:

```text
1.665 lotes adicionais = 333.000 notas
```

Isso levaria o total materializado representado para:

```text
667.100 + 333.000 = 1.000.100 notas
```

## Recomendação operacional

Para manter simplicidade e alinhamento com o ledger de 1 milhão, a melhor próxima meta é consolidar a sequência de lotes até:

```text
lote-5000
```

Isso adiciona:

```text
1.700 lotes
340.000 notas
```

e completa:

```text
5.000 lotes sequenciais × 200 notas = 1.000.000 notas materializadas sequenciais
```

## Atenção ao tamanho

A rodada anterior de 500.000 notas gerou cerca de 636,7M antes do merge/poda. Para os 340.000 restantes, uma estimativa proporcional é:

```text
340.000 / 500.000 × 636,7M ≈ 433M antes do merge/poda
```

Portanto, a próxima etapa deve continuar usando:

- geração em pacotes compactados;
- merge completo incremental;
- poda dos zips intermediários depois da validação;
- checksums;
- evitar criar centenas de milhares de Markdown ativos no workspace.

## Segurança

Os domínios `cannabis-medicinal` e `micologia` continuam restritos a conteúdo educacional, documental, científico, regulatório, rastreabilidade e perguntas para profissionais habilitados. Conteúdo operacional regulado deve permanecer `0`.
