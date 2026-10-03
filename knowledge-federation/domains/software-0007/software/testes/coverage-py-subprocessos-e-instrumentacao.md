---
id: software.testes.tranche15.000873
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-02
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: "2026-10-02"
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-15.md"
fontes: ["https://coverage.readthedocs.io/en/latest/subprocess.html", "https://coverage.readthedocs.io/en/latest/commands/cmd_combine.html"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# coverage.py: propagar medição a subprocessos de forma configurada

## Em uma frase
A opção [run] patch = ["subprocess"] (ou a sintaxe INI equivalente) inicia coverage em processos Python criados por subprocess, os.system e famílias execv/spawnv.

## Por que importa
Essa via ainda exige parallel = true e coverage combine antes do relatório.

## Como funciona
Como estratégia manual separada, defina COVERAGE_PROCESS_START, faça Python chamar coverage.process_startup() na inicialização e propague a variável para o processo filho.

## Exemplo
No TOML, configure patch = ["subprocess"] e parallel = true; execute o pai e um filho que rode uma linha exclusiva, depois faça coverage combine antes do relatório. Se usar manualmente exec*e/spawn*e com ambiente novo, propague o caminho absoluto do arquivo em COVERAGE_PROCESS_START.

## Limites e trade-offs
A estratégia manual exige invocar process_startup() quando Python inicia; as variantes exec*e/spawn*e recebem um ambiente novo e precisam receber explicitamente COVERAGE_PROCESS_START. Processos que não encerram normalmente também podem não gravar os dados.

## Como verificar
Execute um filho Python por subprocess e confirme sua linha exclusiva após coverage combine; repita com ambiente controlado e verifique a variável/configuração quando usar uma variante que substitui o ambiente.

## Conexões
- [[coverage-py-combinar-dados-de-multiplos-processos]] — Veja também: coverage.py: combinar arquivos paralelos antes de interpretar a cobertura.
- [[coverage-py-branch-partial-e-pragma-no-branch]] — Veja também: coverage.py: usar pragma no branch para desvios estruturalmente parciais.

## Fontes
- [Coverage.py 7.16.2 — Managing processes](https://coverage.readthedocs.io/en/latest/subprocess.html) — instrumentação de subprocessos, multiprocessing, ambiente e combinação; consultado em 2026-10-02.
- [Coverage.py 7.16.2 — Combining data files](https://coverage.readthedocs.io/en/latest/commands/cmd_combine.html) — arquivos paralelos, combinação, remoção de entradas antigas e remapeamento de caminhos; consultado em 2026-10-02.
