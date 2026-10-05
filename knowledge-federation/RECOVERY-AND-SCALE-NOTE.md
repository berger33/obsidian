# Retomada pós-merge: escala com qualidade

Atualizado em 2026-10-04. A meta ativa é **500 lotes × 2.000 notas substantivas = 1.000.000 de notas válidas**. Revisão humana não é obrigatória para novas notas; revisão factual por IA é aceita somente quando registrada separadamente, com relatório.

## Estado editorial atual

O checkpoint legado e os arquivos antigos seguem como histórico e não contam como progresso. No diretório ativo `knowledge-federation/domains/` há **6640 arquivos**: 100 legados com pendências e **6540 notas válidas** pelo protocolo (49 aprovações humanas históricas + 6491 revisões factuais por IA). Os lotes 1–3 estão completos; o quarto lote `software-criacao-ia-2000-0004` tem 500/2.000 notas válidas após a tranche 5, com relatório factual, gate e reconciliação próprios.

## Decisão técnica e estados

Manter inventário e conteúdo separados, sem confundir catálogo com conhecimento:

1. **catalogada** — ID e taxonomia; não conta como conteúdo;
2. **candidata** — nota substantiva e gate automatizado aprovado;
3. **validada** — fontes/afirmações confrontadas e revisão factual registrada por pessoa ou IA, com tipo e responsável explícitos;
4. **rejeitada/needs-review** — não contabilizada até correção e revisão.

Materializar um arquivo Markdown não muda seu estado. Revisão por IA não é aprovação humana. Geradores de sementes servem ao planejamento, não à contagem de notas válidas.

## Ferramentas e comandos

- `scripts/note_quality.py` — regras reutilizáveis de gate e distinção de revisões.
- `scripts/audit_note_quality.py` — auditoria de arquivos ativos e do checkpoint SQLite compactado.
- `scripts/audit_batch.py` — só marca lote `complete` quando todas as notas passam gate e têm revisão factual registrada.
- `tests/test_note_quality.py` — regressões do gate para conteúdo, fontes, links e metadata de revisão.

```bash
python3 -m unittest discover -s knowledge-federation/tests -v
python3 knowledge-federation/scripts/audit_note_quality.py \
  --path knowledge-federation/domains \
  --archive knowledge-federation/archives/ledger-v1000000-mat8000.sqlite.xz
```

## Próximo ciclo

1. Manter como concluídos os três primeiros lotes de 2.000 notas qualificadas.
2. Continuar o lote `software-criacao-ia-2000-0004` com seleção de tópicos e fontes primárias para a próxima tranche de 100; IDs ainda não produzidos não são reservados.
3. Após cada tranche, rodar gate, testes e auditorias; reconciliar manifesto, MOC, fila e métricas antes de contar.
4. Não abrir o lote 5 automaticamente; avaliar cobertura e pedido do usuário.
5. Publicar o relatório final apenas após atingir 1.000.000 de notas válidas.
