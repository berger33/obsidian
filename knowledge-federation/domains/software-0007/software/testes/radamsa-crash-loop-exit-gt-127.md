---
id: software.testes.tranche25.001887
tipo: tecnica
dominio: software
subdominio: testes
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-03
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-03
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-testes-2000-0001-tranche-25.md"
fontes: ["https://gitlab.com/akihe/radamsa/-/raw/master/README.md", "https://gitlab.com/akihe/radamsa"]
tags: [dominio/software, subdominio/testes, qualidade/candidata]
lote: software-testes-2000-0001
---

# O laço shell de captura de falha: arquivo fuzzed e código de saída > 127

## Em uma frase
Para testar cada saída em uma execução isolada e guardar o caso que causou o crash, o README mostra o padrão clássico em shell: gravar radamsa sample.gz > fuzzed.gz, executar gzip -dc fuzzed.gz > /dev/null e verificar test $? -gt 127 && break dentro de um laço while true.

## Por que importa
Em sistemas UNIX, quando um programa simples termina de forma fatal por sinal (como SIGSEGV, SIGABRT ou SIGFPE), o shell reporta um código de saída acima de 127 (128 + número do sinal); testar $? -gt 127 separa crashes reais de erros normais de validação (código 1 ou 2) que são esperados quando a entrada está corrompida.

## Como funciona
Grave a saída mutada em um arquivo em disco (como fuzzed.gz) antes de invocar o binário alvo e interrompa o laço com test $? -gt 127 && break para que o arquivo causador do crash permaneça salvo no diretório para depuração.

## Exemplo
No script do README — while true; do radamsa sample.gz > fuzzed.gz; gzip -dc fuzzed.gz > /dev/null; test $? -gt 127 && break; done —, quando o laço para, fuzzed.gz contém exatamente a entrada que derrubou o processo.

## Limites e trade-offs
O próprio README ressalva que esse teste de código de saída maior que 127 é uma forma simples voltada a programas single-threaded simples; alvos que capturam sinais internamente ou rodam em processos filhos exigem monitoramento adicional.

## Como verificar
Conferi o bloco final de script while true com test $? -gt 127 && break no README oficial do Radamsa.

## Conexões
- [[radamsa-multiple-outputs-flag-n]] — Veja também: Geração de múltiplas saídas com -n e unicidade estatística.
- [[radamsa-streaming-vs-per-run-tradeoff]] — Veja também: Trade-off entre fuzzing em pipe contínuo e uma execução por arquivo.

## Fontes
- [Radamsa — README oficial (A Crash Course to Radamsa)](https://gitlab.com/akihe/radamsa/-/raw/master/README.md) — README oficial do Radamsa com proposta black-box, origem no Protos Genome Project, build de binário único, uso em pipe como cat, semente -s/--seed, mutador numérico, -n e laço de captura de crash.; consultado em 2026-10-03.
- [Repositório oficial akihe/radamsa no GitLab](https://gitlab.com/akihe/radamsa) — Repositório oficial do Radamsa no GitLab com código-fonte, Makefile, mutadores e documentação.; consultado em 2026-10-03.
