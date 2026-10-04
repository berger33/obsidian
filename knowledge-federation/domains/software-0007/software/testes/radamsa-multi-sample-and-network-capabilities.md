---
id: software.testes.tranche25.001889
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

# Amostras múltiplas e modos TCP cliente/servidor

## Em uma frase
O README registra duas capacidades estruturais além do filtro básico de um único arquivo: quando recebe mais de um arquivo de amostra, o Radamsa usa um ou alguns deles para compor uma saída, e a ferramenta também possui suporte embutido para atuar como servidor ou cliente TCP quando necessário.

## Por que importa
Misturar trechos de mais de uma amostra válida permite recombinar cabeçalhos e corpos de arquivos diferentes do mesmo formato, enquanto o modo TCP evita escrever wrappers de socket com netcat para enviar entradas mutadas a serviços de rede.

## Como funciona
Passe um diretório ou glob de amostras válidas variadas na linha de comando para permitir recombinação entre arquivos e consulte radamsa --help quando o alvo esperar conexões como cliente ou servidor TCP.

## Exemplo
Em vez de manter apenas um sample.gz, fornecer um conjunto de arquivos de exemplo representativos dá ao gerador mais blocos estruturais para combinar em cada saída.

## Limites e trade-offs
O trecho inicial do README menciona o suporte a TCP e a combinação de múltiplos arquivos em alto nível e remete ao radamsa --help para a lista detalhada de flags de linha de comando.

## Como verificar
Conferi as menções a múltiplos arquivos e a servidor/cliente TCP na seção Fuzzing with Radamsa do README oficial.

## Conexões
- [[radamsa-streaming-vs-per-run-tradeoff]] — Veja também: Trade-off entre fuzzing em pipe contínuo e uma execução por arquivo.

## Fontes
- [Radamsa — README oficial (A Crash Course to Radamsa)](https://gitlab.com/akihe/radamsa/-/raw/master/README.md) — README oficial do Radamsa com proposta black-box, origem no Protos Genome Project, build de binário único, uso em pipe como cat, semente -s/--seed, mutador numérico, -n e laço de captura de crash.; consultado em 2026-10-03.
- [Repositório oficial akihe/radamsa no GitLab](https://gitlab.com/akihe/radamsa) — Repositório oficial do Radamsa no GitLab com código-fonte, Makefile, mutadores e documentação.; consultado em 2026-10-03.
