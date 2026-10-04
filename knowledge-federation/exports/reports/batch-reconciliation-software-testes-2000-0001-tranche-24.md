# Reconciliação — `software-testes-2000-0001`, tranche 24

Data: 2026-10-03

Resultado: **100 notas contabilizadas após gate e revisão factual por IA**. Esta reconciliação não representa aprovação humana.

## Escopo da tranche

- IDs: **1760–1859**, 100 arquivos em dez grupos temáticos com dez notas cada; conteúdo substantivo de **279–394 palavras por nota**, conforme o construtor.
- Fontes e dados reproduzíveis: [`_build_tranche24.py`](../../scripts/_build_tranche24.py) e [`_tranche24_data/`](../../scripts/_tranche24_data/).
- Relatório de revisão: [`ai-review-software-testes-2000-0001-tranche-24.md`](ai-review-software-testes-2000-0001-tranche-24.md). Registra 100 decisões factuais por IA, sem alterar as 49 aprovações humanas históricas.
- Grupos: Robot Framework, Pynguin, Kani, Honggfuzz, LibAFL, syzkaller, Behat, Cucumber-JVM, FuzzBench e httpmock.
- Contexto de retomada: esta tranche continua a série a partir da tranche 23; a política de conteúdo permanece a mesma das tranches anteriores (gate automatizado + revisão factual registrada; revisão por IA nunca rotulada como humana).

## Auditorias e resultados

| Verificação | Resultado |
|---|---|
| Gate do lote de testes de software | **1859/1859 aprovadas**; 0 pendências. A auditoria específica incluiu as 1759 notas anteriores e as 100 novas. |
| Gate das notas novas | **100/100 aprovadas**; mínimo de 100 palavras por nota, seções obrigatórias e duas fontes HTTPS específicas (com caminho próprio) por nota. |
| Revisão factual do lote | **9 humanas históricas + 1850 por IA**; separação preservada. As novas 100 foram revisadas por IA. |
| Testes automatizados do repositório | **12 aprovados** (`python -m unittest discover -s knowledge-federation/tests`). |
| Auditoria global por arquivos | **1999 Markdown ativos**, 1899 válidos (49 humanas + 1850 IA) e 100 legados com pendências, excluídos da contagem. O ledger mantém 1.000.000 registros-template e não contribui para notas válidas. |
| Fila de revisão | Posições **nº 50–1899** com exatamente uma linha `APROVADA POR IA` cada (1850 linhas); as 100 linhas novas (1800–1899) correspondem às notas 1760–1859. |
| IDs, títulos, slugs e conteúdo duplicado | 100 IDs únicos no intervalo; sem colisão de slug/título com o inventário ativo; nenhum corpo idêntico. Similaridade Jaccard de shingles de cinco palavras no texto completo (frontmatter excluído): média **0,0011** contra amostra de 400 notas de outros lotes/grupos e **0,0150** dentro da tranche. No corpo substantivo (sem `## Fontes` nem `## Conexões`) as médias caem para **0,0002** e **0,0014**, com máximo **0,0415** (par interno `fuzzbench-reporting-library` × `fuzzbench-three-pieces`, que cita a mesma linha do README oficial sobre a biblioteca de reporting). |
| Frases substantivas repetidas | Nenhuma repetição entre as notas 1760–1859 (gate de prosa do construtor). |
| Links relativos | **7386 vínculos relativos verificados** nos documentos reconciliados e nas 1859 notas do lote (wikilinks resolvidos contra o vault inteiro), todos com alvos resolvidos — incluindo os vínculos ao presente relatório criados pela própria reconciliação; 0 quebrados. |

Relatórios reproduzíveis: [qualidade do lote](note-quality-software-testes-2000-0001.md), [qualidade global](note-quality-audit.md) e [auditoria rápida do inventário](global-audit-fast.md). A auditoria rápida mostra zeros do SQLite local vazio; isso **não** substitui a contagem editorial por arquivos acima.

## Conferência de fontes e escopo factual

As afirmações foram comparadas ao conteúdo das fontes primárias capturadas para cada grupo:

- **Robot Framework — automação genérica em texto puro para aceitação e RPA** (itens 1760–1769): Conferi o `README.rst` oficial no repositório `robotframework/robotframework` (introdução, instalação via `pip`, pins 6.1.1/4.1.3 para versões legadas de Python/Jython/IronPython, exemplo de suíte `Valid Login`, uso de `robot` e `rebot`, ecossistema, Robot Framework Foundation e duplo licenciamento Apache 2.0 / CC-BY 3.0) e a página do repositório no GitHub antes de redigir as dez notas.
- **Pynguin — geração automática de testes unitários para Python** (itens 1770–1779): Conferi o README na página oficial do PyPI (proposta, pré-requisitos Python 3.10 com 3.11–3.14 experimentais, aviso de execução do módulo sob teste, instalação, exemplo de linha de comando, governança na Universidade de Passau e licença MIT) e a página Quickstart oficial no Read the Docs (variável `PYNGUIN_DANGER_AWARE`, isolamento com `pynguin-docker.sh`, exemplo `triangle` com anotações PEP 484 e log interno com `Algorithm.DYNAMOSA` e fallback timeout de 600s) antes de redigir as dez notas.
- **Kani — model checker bit-preciso para Rust** (itens 1780–1789): Conferi o README oficial do repositório `model-checking/kani` (definição, checagens de safety em blocos `unsafe` e correctness como panics/overflows/asserts/contracts experimentais, instalação com `cargo install --locked kani-verifier` e `cargo kani setup`, exemplo de harness `#[kani::proof]` com `kani::any()`, GitHub Action, citação ASE 2026 com `CITATION.cff` e licenciamento duplo MIT/Apache-2.0) antes de redigir as dez notas.
- **Honggfuzz — fuzzer orientado a segurança com cobertura de hardware** (itens 1790–1799): Conferi o README oficial do repositório `google/honggfuzz` (definição, cobertura de hardware Intel BTS/PT e software, modo persistente `-P` até 1M/seg, início com corpus vazio, monitoramento via `ptrace`, suporte multiplataforma, build com wrappers `hfuzz-clang`/`hfuzz-clang++`, placeholder `___FILE___`, lista de trophies por software, projetos adotantes e disclaimer Apache 2.0) antes de redigir as dez notas.
- **LibAFL — a biblioteca Rust para montar o próprio fuzzador** (itens 1800–1809): Conferi o README oficial do repositório `AFLplusplus/LibAFL` (proposta, cinco destaques incluindo `LLMP` e `BytesInput` substituível, suporte `no_std`, crates e quatro backends de instrumentação `SanitizerCoverage`/`Frida`/`QEMU`/`TinyInst`, dependências LLVM 15–18 e `just`, exemplos em `fuzzers/` com `libfuzzer_libpng`, paper CCS '22, `DEBUGGING.md`/`CONTRIBUTING.md` e licenciamento duplo MIT/Apache-2.0) antes de redigir as dez notas.
- **syzkaller — fuzzer não supervisionado de kernels** (itens 1810–1819): Conferi o README oficial do repositório `google/syzkaller` (definição, SOs suportados, mapa da documentação por kernel, `found_bugs` por sistema, badges e disclaimer) e a página `docs/usage.md` (`syz-manager -config`, painel HTTP, reprodução automática em 4 VMs por padrão, reproducers em formato syzkaller ou C, tempo de reprodução de minutos a uma hora, `hub` e reporting) antes de redigir as dez notas.
- **Behat — BDD em Gherkin para PHP** (itens 1820–1829): Conferi o README oficial do repositório `Behat/Behat` (instalação via Composer com `--dev`, versão de desenvolvimento `bin/behat`, versionamento SemVer v2.0.0 e política de BC para interfaces e service constants, links e mantenedores voluntários) e a página inicial da documentação oficial em `docs.behat.org` (definição, exemplo Gherkin com `Feature`/`Background`/`Scenario`, cobertura de aplicação inteira, mistura de abordagens, `profiles`/`tags`/`suites`, componentes Symfony e sistema de extensões) antes de redigir as dez notas.
- **Cucumber-JVM — Cucumber em linguagem natural para a JVM** (itens 1830–1839): Conferi o README oficial do repositório `cucumber/cucumber-jvm` (proposta, implementação Java, execução com ferramentas de escolha e contêineres de DI, starters Maven/Gradle e repositório de exemplos, artefato no Maven Central, política de upgrade com `release-notes` e `CHANGELOG.md`, canais de suporte, modelo voluntário, duas portas de contribuição e badges de CI/OpenSSF Scorecard/OpenCollective) antes de redigir as dez notas.
- **FuzzBench — benchmarking de fuzzers como serviço** (itens 1840–1849): Conferi o README oficial do repositório `google/fuzzbench` (definição de serviço gratuito em escala, os três componentes oferecidos — API de integração, benchmarks de qualquer projeto OSS-Fuzz e biblioteca de reporting com gráficos e testes estatísticos —, fluxo de submissão, escala do sample report com 10 fuzzers × 24 benchmarks × 20 trials × 24h e CSV comprimido, recomendações de leitura, relatórios periódicos, documentação e contatos) antes de redigir as dez notas.
- **httpmock — servidor HTTP de mentira com API fluent para testes em Rust** (itens 1850–1859): Conferi a página oficial da crate `httpmock` 0.8.3 no `docs.rs` (resumo, lista de features, seção Getting Started com `MockServer::start()` e `server.mock(|when, then| ...)`, diagnóstico de falha do `mock.assert()` com diff do request mais similar, structs `When`/`Then`/`Mock`/`Recording`/`ForwardingRule`/`ProxyRule`, trait `MockExt`, modo standalone com Docker e YAML, núcleo assíncrono com APIs sync/async e licença MIT) antes de redigir as dez notas.

Cada nota mantém ressalvas e pelo menos duas URLs oficiais específicas; revisão factual por IA não é garantia de ausência de erro. Links de páginas apenas referenciadas nos READMEs/docs primários (por exemplo `docs/USAGE.md` no Honggfuzz, `docs/setup.md` no syzkaller ou páginas internas de instalação do Cucumber/FuzzBench) foram usados como ponteiro de navegação, sem afirmações além do material efetivamente lido.

## Contagens reconciliadas

- Lote `software-testes-2000-0001`: **1859/2.000 (92,95%)**; 9 aprovações humanas + 1850 revisões factuais por IA; **141 notas materiais restantes**; estado permanece `in_progress`.
- Total global: **1899/1.000.000 (0,1899%)**; 49 aprovações humanas + 1850 revisões factuais por IA. Os 100 arquivos legados com pendências continuam excluídos. Faltam **998.101** notas válidas para a meta.
- O MOC, o manifesto, a fila, os relatórios de qualidade e os resumos ativos foram sincronizados, incluindo as cadeias de vínculo dos relatórios de IA (tranches 2–24) e da reconciliação mais recente (tranche 24). A meta global continua **1.000.000**, sem reativar a meta anterior de 2.000.000.
- Sugestão de tranche 25 (cobertura ainda não atingida no inventário, faltando 141 notas para fechar o lote): ferramentas como Capybara, Mink, radamsa, CBMC, ESBMC, KLEE, SymbiYosys, Creusot, Dredd e Gock — a lista definitiva sai do grep de colisão de prefixos de slug na abertura da próxima tranche.
