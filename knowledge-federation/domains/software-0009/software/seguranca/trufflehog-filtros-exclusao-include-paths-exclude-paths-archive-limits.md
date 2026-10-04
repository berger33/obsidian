---
id: software.seguranca.tranche01.000019
tipo: tecnica
dominio: software
subdominio: seguranca
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-01.md"
fontes: ["https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/README.md", "https://github.com/trufflesecurity/trufflehog/blob/main/CONTRIBUTING.md", "https://github.com/trufflesecurity/trufflehog"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# TruffleHog Filtragem de Escopo e Limites de Arquivos: `--include-paths`, `--exclude-paths` e controle de archives

## Em uma frase
Em repositórios grandes que contêm dumps de teste, diretórios de terceiros (`vendor/`, `node_modules/`) ou artefatos compactados pesados, o TruffleHog oferece as flags **`--include-paths`** (`-i`) e **`--exclude-paths`** (`-x`) (que recebem um arquivo contendo expressões regulares de caminho, uma por linha), além de controles de tamanho e profundidade de pacotes compactados.

## Por que importa
Escanear gigabytes de assets de vídeo, pacotes `vendor/` ou fixtures de teste conhecidas desperdiça tempo de I/O e chamadas de rede.

## Como funciona
Criando um arquivo `.trufflehog-exclude-paths.txt` com padrões regex como `^node_modules/`, `^vendor/` e `\.lock$`, e passando `--exclude-paths .trufflehog-exclude-paths.txt`, o coletor descarta esses caminhos imediatamente na leitura da fonte.

## Exemplo
```bash
cat << 'EOF' > .trufflehog-exclude.txt
^node_modules/
^vendor/
^testdata/mock_keys/
EOF

trufflehog filesystem . --exclude-paths=.trufflehog-exclude.txt --results=verified
```

## Limites e trade-offs
Lembre-se de que `--exclude-paths` e `--include-paths` esperam o **caminho para um arquivo** contendo as expressões regulares (uma por linha), e não a expressão regular diretamente na linha de comando.

## Como verificar
Execute com `-v` (nível de verbosidade 2+) para verificar nos logs estruturados quais arquivos foram ignorados pelo filtro.

## Conexões
- [[trufflehog-arquitetura-concorrencia-process-flow-chunks-decoders-detectors]] — Veja também: TruffleHog Arquitetura Interna de Concorrência: pipeline de `Sources`, `Chunks`, `Decoders`, `Aho-Corasick` e `Detectors`.
- [[trufflehog-varredura-postman-jenkins-elasticsearch-jira-slack-enterprise]] — Veja também: TruffleHog Além do Git: varredura de `Postman`, `Jenkins`, `Elasticsearch`, `Syslog` e ecossistema colaborativo.

## Fontes
- [TruffleHog GitHub — README.md (4 Pillars: Discovery, Classification, Validation & Analysis, --results Filters, CI/CD & Custom Detectors)](https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/README.md) — README oficial do trufflesecurity/trufflehog documentando os 4 pilares, verificação ativa de credenciais, exit code 183 com --fail, verificação Cosign e detectores customizados; consultado em 2026-10-03.
- [TruffleHog GitHub — CONTRIBUTING.md (Architecture of Pipeline Stages, Aho-Corasick Keyword Matching, Detectors & Verification)](https://github.com/trufflesecurity/trufflehog/blob/main/CONTRIBUTING.md) — Guia técnico de arquitetura do TruffleHog detalhando o pipeline concorrente Source -> Chunker -> Matcher Aho-Corasick -> Detector -> Verifier -> Dispatcher; consultado em 2026-10-03.
- [TruffleHog — Official GitHub Repository (Truffle Security)](https://github.com/trufflesecurity/trufflehog) — Repositório oficial open-source do TruffleHog; consultado em 2026-10-03.
