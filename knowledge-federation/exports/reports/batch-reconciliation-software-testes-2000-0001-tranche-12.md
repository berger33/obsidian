# Reconciliação do lote `software-testes-2000-0001` — tranche 12

- Data: 2026-10-02
- Escopo: IDs 550–649; manifesto, relatório factual por IA, fila de revisão, MOC e auditorias.
- Método: inspeção dos 100 arquivos de dados e notas geradas, confronto das afirmações com documentação oficial dos dez projetos, gate determinístico, resolução de wikilinks e revisão de sentenças repetidas. A revisão factual por IA não é aprovação humana.

## Resultado

- **Revisão factual concluída: 100/100 notas.** Foram conferidos Playwright, Hypothesis, TestNG, Go `testing`, PIT, PHPUnit 12.5, RSpec 3.13, ExUnit 1.20.4, Newman e axe-core. Cada nota está ligada à sua fonte principal no [relatório factual da tranche 12](ai-review-software-testes-2000-0001-tranche-12.md); as fontes secundárias estão no frontmatter e na seção Fontes de cada nota.
- **Correções factuais aplicadas antes do registro final:** ciclo de fixtures do PHPUnit ajustado para instância nova por método; ressalva de `DoesNotPerformAssertions` restringida ao sinal de teste arriscado; explicação de `--bail failure` do Newman especifica o encerramento após o script atual e distingue supressão do exit code; typo `Matchers` corrigido em RSpec; nota axe-core esclarece que `node.target` é uma coleção e deve ser passada ao `axe.run` no formato de contexto apropriado.
- **Fontes:** os links Hypothesis e Postman foram atualizados para referências canônicas atuais. A documentação axe-core confirma que os alvos de resultado podem ser seletores ou arrays aninhados para frames/shadow DOM e que alvos anteriores podem ser reexecutados com `axe.run(targets)`.
- **Substância e gate:** as 100 notas têm **193–246 palavras**, duas fontes HTTPS específicas e as seções requeridas. O [relatório de qualidade do lote](note-quality-software-testes-2000-0001.md) registra **649/649** notas candidatas aprovadas, sem pendências; as nove aprovações humanas históricas foram preservadas e 640 revisões factuais por IA permanecem separadas.
- **Repetição:** a varredura independente do corpo de 649 notas no subdomínio não encontrou sentença substantiva exata repetida envolvendo a tranche 12. O builder também passou seu gate interno de conteúdo e repetição.
- **Manifesto:** **649 entradas numeradas e contínuas (1–649)**; a nova tranche lista 100 destinos únicos (IDs 550–649) existentes no lote.
- **Fila de revisão:** 100 registros novos de revisão por IA nas posições 590–689, associados um a um às notas 550–649. As **49 aprovações humanas históricas** foram preservadas sem alteração e não foram estendidas à tranche.
- **MOC:** as 100 notas aparecem uma vez sob os dez grupos novos; o índice é navegação, não validação factual.
- **Auditoria de qualidade do subdomínio:** 649 arquivos; 649 aprovados no gate; 9 com revisão factual humana histórica e 640 com revisão factual por IA identificada; 0 pendências.
- **Auditoria global:** 789 arquivos Markdown ativos; 689 válidos (49 humanos + 640 IA); 100 legados permanecem pendentes fora da contagem.
- **Verificação final:** **12 testes passaram** em `python3 -m unittest discover -s knowledge-federation/tests -v`; `py_compile`, as auditorias local/global e `git diff --check` passaram após a reconciliação documental.
- **Lote ainda em andamento:** **649/2.000** notas válidas; faltam **1.351** notas materiais. Esta tranche não conclui o lote.

## Escopo e ressalvas

O `audit_batch.py` existente lê lotes registrados no SQLite. O lote ativo desta reconciliação é mantido no manifesto Markdown e não possui linha de lote no ledger local; por isso, a auditoria DB-backed não foi apresentada como passe nem foram criadas linhas SQLite para simular sucesso. A contagem usa somente arquivos materiais, frontmatters e relatórios registrados.

O gate automatizado verifica estrutura, conteúdo mínimo, fontes HTTPS específicas e wikilinks; ele não comprova sozinho a veracidade nem a qualidade editorial. A detecção de repetição cobre sentenças substantivas exatamente iguais, não toda semelhança semântica. A revisão factual por IA permanece separada da revisão humana e não garante ausência absoluta de erros.

## Artefatos de suporte

- [Manifesto ativo](../batches/software-testes-2000-0001.md)
- [Gate do lote e resolução de wikilinks](note-quality-software-testes-2000-0001.md)
- [Auditoria global por arquivos](note-quality-audit.md)
- [Relatório factual por IA da tranche 12](ai-review-software-testes-2000-0001-tranche-12.md)
- [Fila de revisão humana e por IA](human-review-queue.md)
- [MOC de navegação](../../00-home-vault/MOCs/MOC-Testes-Software-0007.md)
