# Reconciliação — `software-criacao-ia-2000-0004`, tranche 1

Data: 2026-10-04. Esta reconciliação contabiliza somente os arquivos substantivos já produzidos na primeira tranche; o estado inicial de abertura continua preservado em [`batch-reconciliation-software-criacao-ia-2000-0004-initial.md`](batch-reconciliation-software-criacao-ia-2000-0004-initial.md).

## Escopo e resultado da tranche

- IDs materiais: `software.criacao_ia.tranche01.000001` a `software.criacao_ia.tranche01.000100`.
- Arquivos de nota: **100**, no diretório `domains/software-0010/software/criacao-ia/`.
- Seleção: **10 trilhas × 10 notas**, detalhadas abaixo e no manifesto/MOC.
- Gate da tranche: **100/100 aprovadas**; mínimo de 100 palavras, duas fontes HTTPS específicas por nota, seções obrigatórias e wikilinks resolvidos.
- Revisão factual por IA: **100/100**, registrada em `revisao_ia: aprovada`, com revisor, data e relatório.
- Revisão humana: **0/100**; nenhuma aprovação humana foi solicitada, registrada ou inferida.
- Contabilizadas no lote: **100/2.000 (5,00%)**; estado permanece `in_progress`.
- Próximas notas: **1.900** ainda não produzidas; não há IDs futuros reservados, placeholders ou progresso virtual.

## Trilhas selecionadas

1. Programação assistida com GitHub Copilot: prompts verificáveis, contexto, modos de IDE, tarefas pequenas, geração/revisão de testes e inspeção do diff.
2. OpenAI Responses API: integração de texto, instruções, versionamento de prompts, tratamento de estados e avaliação.
3. Function calling e Structured Outputs: contratos, correlação de chamadas, validação, autorização, efeitos colaterais e falhas.
4. Unity ML-Agents 4.0: agentes, observações, ações, recompensas, episódios, treinamento e inferência.
5. Unreal Engine Behavior Trees/EQS: Blackboard, composições, Decorators, Tasks, consultas, testes espaciais e depuração.
6. Godot Navigation: malha, caminho, sincronização, waypoints, evasão local e validação com movimento real.
7. Blender e glTF: Actions, clips, NLA, rigs, intervalos, compatibilidade, exportação e testes dentro do jogo.
8. Unreal Sequencer/Movie Render Pipeline: tracks, câmeras, shots, captura de takes, jobs, presets e revisão do render.
9. ComfyUI/Wan 2.2: grafos, modelos, templates, geração de vídeo, parâmetros, workflow versionado e aprovação de assets.
10. Documentação técnica: tutorial/how-to/referência/explicação, público, versões, exemplos reproduzíveis, acessibilidade e revisão de conteúdo produzido por IA.

As notas usam documentação primária específica dos projetos e APIs listados em cada arquivo. A documentação oficial vigente do pacote Unity ML-Agents 4.0 foi usada; páginas legadas marcadas como deprecated não foram citadas. Recomendações de produto, segurança e validação estão separadas de afirmações de comportamento dos fornecedores.

## Evidências

- [Manifesto do lote e lista dos IDs/títulos](../batches/software-criacao-ia-2000-0004.md)
- [MOC do lote](../../00-home-vault/MOCs/MOC-Criacao-IA-Software-0010.md)
- [Revisão factual por IA, nota por nota](ai-review-software-criacao-ia-2000-0004-tranche-01.md)
- [Gate por arquivos da tranche](note-quality-software-criacao-ia-2000-0004-tranche-01.md)
- [Registro separado de revisões](human-review-queue.md), registros numerados 6041–6140
- [Auditoria global por arquivos e checkpoint](note-quality-audit.md)
- [Auditoria global rápida](global-audit-fast.md)
- `python3 -m unittest discover -s knowledge-federation/tests -v`: **13 testes aprovados**.

## Reconciliação global após a tranche

| Métrica | Antes da tranche | Depois da tranche |
|---|---:|---:|
| Arquivos Markdown ativos em `domains/` | 6.140 | 6.240 |
| Notas válidas pelo protocolo | 6.040 | 6.140 |
| Aprovações humanas históricas | 49 | 49 |
| Revisões factuais por IA | 5.991 | 6.091 |
| Notas legadas com pendências, fora da contagem | 100 | 100 |
| Lotes completos | 3/500 | 3/500 |
| Lote 4 `software-criacao-ia-2000-0004` | 0/2.000 | 100/2.000 |

A auditoria global avaliou **6.240 arquivos**: 6.140 passaram o protocolo atual (49 revisões humanas históricas + 6.091 revisões por IA) e 100 notas legadas mantêm pendências. O checkpoint contém 1.000.000 de registros virtuais com template e 8.000 caminhos materializados; nenhum deles foi incluído na contagem editorial. A tranche 1 não altera o status `complete` dos três lotes anteriores nem abre o lote 5.
