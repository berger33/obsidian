# Reconciliação — `software-criacao-ia-2000-0004`, tranche 5

Data: 2026-10-04. Esta reconciliação contabiliza somente as 100 notas materiais da tranche 5 (IDs 401–500). Preserva as reconciliações anteriores [`tranche 1`](batch-reconciliation-software-criacao-ia-2000-0004-tranche-01.md), [`tranche 2`](batch-reconciliation-software-criacao-ia-2000-0004-tranche-02.md), [`tranche 3`](batch-reconciliation-software-criacao-ia-2000-0004-tranche-03.md) e [`tranche 4`](batch-reconciliation-software-criacao-ia-2000-0004-tranche-04.md).

## Escopo, seleção e resultado

- IDs materiais: `software.criacao_ia.tranche05.000401` a `software.criacao_ia.tranche05.000500`.
- Arquivos novos: **100 notas**; o diretório `domains/software-0010/software/criacao-ia/` passa de 400 para 500 notas deste lote.
- Seleção: **10 grupos × 10 notas**. Antes da geração, `git ls-files knowledge-federation/domains/software-0010/software/criacao-ia/` forneceu o inventário de 400 notas; títulos/slugs candidatos foram comparados com o inventário e pesquisados no vault inteiro. Resultado: **0 slugs ou títulos exatos duplicados**.
- Cobertura próxima foi mantida distinta: notas ComfyUI anteriores tratam workflows/produção; esta tranche trata a Server API. Ollama anterior cobre configuração local, `num_ctx`, `keep_alive` e embeddings no Continue.dev; esta tranche cobre contratos REST. Também foram encontrados temas adjacentes de Storybook/MSW/Backstage, importação genérica de assets Godot e Unity ECS, sem repetir esses focos.
- Gate final por arquivo: **100/100 aprovadas**, 209–301 palavras por nota, exatamente duas fontes HTTPS específicas e wikilinks resolvidos. O gate foi repetido depois do registro factual; evidência em [`note-quality-software-criacao-ia-2000-0004-tranche-05.md`](note-quality-software-criacao-ia-2000-0004-tranche-05.md).
- Revisão factual por IA: **100/100**, com registro por ID em [`ai-review-software-criacao-ia-2000-0004-tranche-05.md`](ai-review-software-criacao-ia-2000-0004-tranche-05.md). A revisão humana é **0/100**; as 49 aprovações humanas históricas permanecem inalteradas.
- Auditoria de links: **200 referências** em 100 notas, todas HTTPS; relatório [`source-link-audit-software-criacao-ia-2000-0004-tranche-05.md`](source-link-audit-software-criacao-ia-2000-0004-tranche-05.md). O relatório distingue a resolução interna do gate da checagem HTTP externa e documenta respostas TLS não conclusivas do sandbox.
- Contagem do lote 4: **500/2.000 (25,00%)**. Permanecem 1.500 notas não produzidas; nenhum ID futuro foi atribuído ou reservado e o lote 5 não foi aberto.

## Grupos selecionados

1. Ollama REST API: endereçamento, payloads, catálogo e ciclo dos modelos
2. ComfyUI Server API: exportar workflows, enfileirar execuções e recuperar resultados
3. Godot EditorImportPlugin: registrar importadores, definir contratos e salvar recursos
4. Unity Sentis 2.5: preparar tensores, escolher backend e integrar inferência ao frame loop
5. OpenAI Realtime API: áudio em tempo real, turnos, eventos e chamadas de ferramenta
6. Vercel AI SDK UI: estado de chat, persistência, ferramentas e protocolos de stream
7. Storybook: produzir histórias tipadas, mocks de UI e verificações automatizadas
8. Docusaurus 3.10: estruturar, versionar e localizar sites de documentação
9. Ink: integrar narrativa interativa compilada com o runtime do jogo
10. Unity Addressables 2.7: carregar, baixar, versionar e liberar conteúdo remoto

## Evidências e artefatos

- [Manifesto do lote, métricas e IDs/títulos](../batches/software-criacao-ia-2000-0004.md)
- [MOC do lote](../../00-home-vault/MOCs/MOC-Criacao-IA-Software-0010.md)
- [Auditoria de links externos e wiki](source-link-audit-software-criacao-ia-2000-0004-tranche-05.md)
- [Gate final da tranche](note-quality-software-criacao-ia-2000-0004-tranche-05.md)
- [Revisão factual por IA, registro por nota](ai-review-software-criacao-ia-2000-0004-tranche-05.md)
- [Fila separada de revisão humana](human-review-queue.md), linhas 6441–6540 (decisões IA não são aprovações humanas)
- [Auditoria global de qualidade e checkpoint](note-quality-audit.md), executada após esta reconciliação conforme o protocolo.

## Reconciliação global após a tranche

| Métrica | Antes | Depois |
|---|---:|---:|
| Arquivos Markdown ativos em `domains/` | 6.540 | 6.640 |
| Notas válidas pelo protocolo | 6.440 | 6.540 |
| Aprovações humanas históricas | 49 | 49 |
| Revisões factuais por IA | 6.391 | 6.491 |
| Notas legadas com pendências, fora da contagem | 100 | 100 |
| Lotes completos | 3/500 | 3/500 |
| Lote 4 `software-criacao-ia-2000-0004` | 400/2.000 (20,00%) | 500/2.000 (25,00%) |

Após a tranche, o total é **6.540 notas válidas** (49 humanas históricas + 6.491 revisões factuais por IA) em **6.640 arquivos Markdown ativos**, mantendo as 100 notas legadas fora da contagem. Restam **993.460** notas para a meta de 1.000.000. O checkpoint histórico de 1.000.000 registros virtuais e 8.000 caminhos materializados continua excluído da contagem; o estado `complete` dos três lotes anteriores não muda. As 15 tranches planejadas restantes são cadência, não reserva de IDs. Não abrir lote 5 nem atribuir IDs futuros automaticamente.

## Verificações globais obrigatórias antes de publicar

Executar, conforme `PROMPT-CONTINUACAO.md`, os testes unitários e a auditoria global sobre `knowledge-federation/domains` mais o arquivo de ledger. Os resultados desses comandos não são substituídos pelo gate da tranche.
