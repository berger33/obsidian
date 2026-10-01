# Próximos 100 lotes — relatório histórico de arquivos gerados

Data: 2026-10-01

> Estes totais descrevem arquivos-placeholder derivados do ledger, não notas válidas. A auditoria encontrou texto-template nos 1.000.000 registros virtuais do checkpoint; veja [`STATUS-CONSOLIDACAO-1M.md`](STATUS-CONSOLIDACAO-1M.md).

## Entrega

```text
knowledge-federation/archives/study-vault-next-100-lotes.zip
```

## Resultado

- Lotes executados: **100**
- Arquivos-placeholder por lote: **200**
- Arquivos-placeholder materializados no zip: **20.000**
- Arquivos dentro do zip: **20.105**
- Tamanho do zip: **25.5M**
- Lotes em domínios regulados: **31**
- Conteúdo operacional regulado: **0**
- Teste de integridade do zip: **OK**

## Relatório

```text
knowledge-federation/exports/reports/next-100-lotes-report.md
```

## Por que foi gerado como zip separado?

Para respeitar a arquitetura ledger-first e evitar inflar o workspace com mais 20.000 arquivos ativos. O zip é um vault Obsidian independente: descompacte e abra no Obsidian começando por:

```text
00-Inicio/Home.md
```

## Conteúdo interno

```text
00-Inicio/Home.md
00-Mapas/MOC-lote-*.md
10-Lotes/lote-*/...
_canvas/Mapa-100-Lotes.canvas
_meta/manifest-next-100-lotes.json
_meta/auditoria-next-100-lotes.md
README.md
```

## Observação de segurança

Os lotes de cannabis medicinal e micologia foram renderizados com aviso de domínio regulado e `conteudo_operacional: false`. O uso previsto é estudo, documentação, rastreabilidade, perguntas qualificadas e consulta a profissionais habilitados.
