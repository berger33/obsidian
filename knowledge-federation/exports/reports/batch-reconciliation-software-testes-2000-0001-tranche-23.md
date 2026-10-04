# Reconciliação — `software-testes-2000-0001`, tranche 23

Data: 2026-10-03

Resultado: **100 notas contabilizadas após gate e revisão factual por IA**. Esta reconciliação não representa aprovação humana.

## Escopo da tranche

- IDs: **1660–1759**, 100 arquivos em dez grupos temáticos com dez notas cada; conteúdo substantivo de **284–452 palavras por nota**, conforme o construtor.
- Fontes e dados reproduzíveis: [`_build_tranche23.py`](../../scripts/_build_tranche23.py) e [`_tranche23_data/`](../../scripts/_tranche23_data/).
- Relatório de revisão: [`ai-review-software-testes-2000-0001-tranche-23.md`](ai-review-software-testes-2000-0001-tranche-23.md). Registra 100 decisões factuais por IA, sem alterar as 49 aprovações humanas históricas.
- Grupos: Karma, JUnit 4, ApprovalTests.Java, fuzzing nativo do Go, cargo-fuzz, AFL++, boofuzz, Hyperfoil, Infection e Atheris.
- Contexto de retomada: esta tranche continua a série a partir da tranche 22; a política de conteúdo permanece a mesma das tranches anteriores (gate automatizado + revisão factual registrada; revisão por IA nunca rotulada como humana).

## Auditorias e resultados

| Verificação | Resultado |
|---|---|
| Gate do lote de testes de software | **1759/1759 aprovadas**; 0 pendências. A auditoria específica incluiu as 1659 notas anteriores e as 100 novas. |
| Gate das notas novas | **100/100 aprovadas**; mínimo de 100 palavras por nota, seções obrigatórias e duas fontes HTTPS específicas (com caminho próprio) por nota. |
| Revisão factual do lote | **9 humanas históricas + 1750 por IA**; separação preservada. As novas 100 foram revisadas por IA. |
| Testes automatizados do repositório | **12 aprovados** (`python -m unittest discover -s knowledge-federation/tests`). |
| Auditoria global por arquivos | **1899 Markdown ativos**, 1799 válidos (49 humanas + 1750 IA) e 100 legados com pendências, excluídos da contagem. O ledger mantém 1.000.000 registros-template e não contribui para notas válidas. |
| Fila de revisão | Posições **nº 50–1799** com exatamente uma linha `APROVADA POR IA` cada (1750 linhas); as 100 linhas novas (1700–1799) correspondem às notas 1660–1759. |
| IDs, títulos, slugs e conteúdo duplicado | 100 IDs únicos no intervalo; sem colisão de slug/título com o inventário ativo; nenhum corpo idêntico. Similaridade Jaccard de shingles de cinco palavras no texto completo (frontmatter excluído): média **0,0009** contra amostra de 400 notas de outros lotes/grupos e **0,0073** dentro da tranche. No corpo substantivo (sem `## Fontes` nem `## Conexões`) as médias caem para **0,0001** e **0,0010**, com máximo **0,0190** (par interno `junit4-assertthrows` × `junit4-expected-peril`, que cita a mesma fórmula da documentação oficial). |
| Frases substantivas repetidas | Nenhuma repetição entre as notas 1660–1759 (gate de prosa do construtor). |
| Links relativos | **7000 vínculos relativos verificados** nos documentos reconciliados e nas 1759 notas do lote (wikilinks resolvidos contra o vault inteiro), todos com alvos resolvidos — incluindo os vínculos ao presente relatório criados pela própria reconciliação; 0 quebrados. |

Relatórios reproduzíveis: [qualidade do lote](note-quality-software-testes-2000-0001.md), [qualidade global](note-quality-audit.md) e [auditoria rápida do inventário](global-audit-fast.md). A auditoria rápida mostra zeros do SQLite local vazio; isso **não** substitui a contagem editorial por arquivos acima.

## Conferência de fontes e escopo factual

As afirmações foram comparadas ao conteúdo das fontes primárias capturadas para cada grupo:

- **Karma — executor de testes JavaScript no navegador** (itens 1660–1669): Conferi o README oficial (aviso de descontinuação, lista de adaptadores, sugestões de migração para Jest/Web Test Runner, jasmine-browser-runner e Vitest), a página inicial da documentação (instalação e integração com Angular), o guia de configuração e a referência do arquivo de configuração (padrões de arquivo com minimatch, `client.clearContext`, timeouts `capture/br`/`browserNoActivityTimeout` com a ressalva do Travis) antes de redigir as dez notas.
- **JUnit 4 — o classic API do JUnit** (itens 1670–1679): Conferi a página oficial About (modo de manutenção), o Getting started (jars e `JUnitCore`) e as páginas do wiki — Test fixtures, Matchers and assertThat, Exception testing, Timeout for tests, Rules, Test suites, Categories e Parameterized tests — antes de redigir as dez notas.
- **ApprovalTests.Java — aprovação por snapshot com writer/scrubber** (itens 1680–1689): Conferi o README oficial (proposta de capturar a inteligência humana, exemplo mínimo com `ApprovalTest`, lista de bibliotecas de teste compatíveis, artefato aprovado versionado) e a página Getting started (writers, options) antes de redigir as dez notas.
- **Fuzzing nativo do Go — `go test -fuzz`** (itens 1690–1699): Conferi a página oficial `go.dev/doc/security/fuzz` (requisitos do fuzz target, modos, corpus-semente, timeout de 10s por entrada na doc, causas de falha detectadas e os quatro estágios de minimização) e as páginas de referência de flags do `go test`/`go help testflag` antes de redigir as dez notas.
- **cargo-fuzz — libFuzzer/LLVMcoverage na toolchain Rust** (itens 1700–1709): Conferi o README oficial (`cargo fuzz add`, estrutura `fuzz_targets/`, `cargo fuzz run` com ASan no Linux/macOS, `reduce`/`tmin`/`cmin` citados na doc da ferramenta) e o capítulo de tutorial do Rust Fuzz Book (log de crash com `asan` e `-F` de replay) antes de redigir as dez notas.
- **AFL++ — fork-server, cmplog e campanha em paralelo** (itens 1710–1719): Conferi o README estável (aviso de versão, quickstart em cinco passos, imagem Docker oficial, licença dual) e o `docs/fuzzing_in_depth.md` (escolha do alvo, instrumentação `afl-clang-fast`/`LTO`/`CMPLOG`, sanitizadores recomendados, preparação de corpus com `afl-cmin`/`afl-tmin`, painel do `afl-fuzz`, modo persistent, dictionário e paralelismo com `-M`/`-S`) antes de redigir as dez notas.
- **boofuzz — fuzzing de protocolo com gramática** (itens 1720–1729): Conferi o README oficial (proposta, recursos de geração e detecção), a seção de documentação viva no repositório e o Quickstart do Read the Docs (primitivas `Request`/`Block`/`String`/`Static`, `sessions`, callbacks de pré/pós-requisição, logger e monitor) antes de redigir as dez notas.
- **Hyperfoil — carga distribuída com fases e modelos de usuários** (itens 1730–1739): Conferi a página inicial (proposta e Apache 2.0), a visão geral, os conceitos oficiais (fases, open/closed model, mestres e agentes) e o Quickstart 1 (YAML com `users`, `rampRate`, `constantUsersPerSec`, `payloadStats`, percentis p99) antes de redigir as dez notas.
- **Infection PHP — mutation testing com MSI** (itens 1740–1749): Conferi o guia oficial (os cinco estágios do fluxo, MSI e a tabela de mutadores), a página de instalação (`.phar` vs. Composer com adapters sob demanda) e a referência de CLI (`--threads`, `--configuration`, `--git-diff-filter`/`--git-diff-lines`, loggers GitHub/gitlab, reuse de coverage) antes de redigir as dez notas.
- **Atheris — fuzzing estruturado para Python nativo/C** (itens 1750–1759): Conferi o README oficial (política de versões do Python e wheels no PyPI, harness mínimo com `atheris.Setup`, `instrument`/`instrument_all` e a auditoria de `sys.modules`, erro "no interesting inputs" e a correção por `@atheris.instrument_func`, `FuzzedDataProvider`, relatório de cobertura só em saída graciosa com `coverage.py`) e referências às flags do libFuzzer e ao documento de mutador customizado da estrutura antes de redigir as dez notas.

Cada nota mantém ressalvas e pelo menos duas URLs oficiais específicas; revisão factual por IA não é garantia de ausência de erro. Links de páginas apenas referenciadas (por exemplo `native_extension_fuzzing.md` no Atheris ou o anúncio do Angular Blog no Karma) foram usados como ponteiro de navegação, sem afirmações além do material efetivamente lido. O repositório `google/fuzzing` foi arquivado como somente-leitura em 27/12/2025 — fato registrado na nota do mutador customizado.

## Contagens reconciliadas

- Lote `software-testes-2000-0001`: **1759/2.000 (87,95%)**; 9 aprovações humanas + 1750 revisões factuais por IA; **241 notas materiais restantes**; estado permanece `in_progress`.
- Total global: **1799/1.000.000 (0,1799%)**; 49 aprovações humanas + 1750 revisões factuais por IA. Os 100 arquivos legados com pendências continuam excluídos. Faltam **998.201** notas válidas para a meta.
- O MOC, o manifesto, a fila, os relatórios de qualidade e os resumos ativos foram sincronizados, incluindo as cadeias de vínculo dos relatórios de IA (tranches 2–23) e da reconciliação mais recente (tranche 23). A meta global continua **1.000.000**, sem reativar a meta anterior de 2.000.000.
- Sugestão de tranche 24 (cobertura ainda não atingida no inventário): suítes e ferramentas como WebdriverIO, TestCafe, k6, libafl, syzkaller, Behat, Mink e psalm-test-framework — a lista definitiva sai do grep de colisão de prefixos de slug na abertura da próxima tranche.
