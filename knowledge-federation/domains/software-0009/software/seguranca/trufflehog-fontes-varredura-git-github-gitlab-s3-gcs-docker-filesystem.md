---
id: software.seguranca.tranche01.000012
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

# TruffleHog Fontes de Varredura: inspeção nativa de `git`, `github`, `gitlab`, `s3`, `gcs`, `docker` (camadas OCI) e `filesystem`

## Em uma frase
Ao contrário de ferramentas limitadas a repositórios Git locais, o TruffleHog possui coletores nativos especializados para varrer organizações inteiras no **GitHub** (`trufflehog github --org=...` incluindo issues, PR comments e gists) e **GitLab**, buckets **Amazon S3** e **Google Cloud Storage (GCS)**, imagens de container **Docker/OCI** (`trufflehog docker --image=...`) e sistemas de arquivos.

## Por que importa
Muitas vezes o código-fonte no Git está limpo, mas a imagem Docker publicada no registry contém um arquivo `.npmrc`, `.aws/credentials` ou variável de build esquecida em uma camada intermediária deletada na camada seguinte.

## Como funciona
Ao executar `trufflehog docker --image=ghcr.io/org/app:latest`, o TruffleHog baixa e inspeciona cada camada histórica do manifesto OCI e a configuração da imagem, mesmo que o arquivo tenha sido removido com `rm` em um `RUN` posterior do `Dockerfile`!

## Exemplo
```bash
# Escaneando todas as camadas de uma imagem de container Docker/OCI em busca de credenciais verificadas:
trufflehog docker --image=trufflesecurity/secrets --results=verified

# Escaneando uma organização inteira do GitHub ignorando repositórios arquivados:
trufflehog github --org=minha-org --exclude-archived --results=verified
```

## Limites e trade-offs
Ao varrer organizações grandes do GitHub (`trufflehog github --org=...`), forneça um `--token` de leitura para evitar atingir os limites de taxa (*rate limits*) de requisições não autenticadas da API do GitHub.

## Como verificar
Execute `trufflehog --help` para listar todos os subcomandos de fontes suportados (`git`, `github`, `gitlab`, `docker`, `s3`, `gcs`, `filesystem`, `syslog`, `postman`).

## Conexões
- [[trufflehog-arquitetura-discovery-classification-validation-analysis]] — Veja também: TruffleHog: arquitetura dos 4 pilares (`Discovery`, `Classification`, `Validation` e `Analysis`) para credenciais vazadas.
- [[trufflehog-verificacao-ativa-credenciais-results-verified-unverified-no-verification]] — Veja também: TruffleHog Políticas de Verificação: controle de `--results=verified,unknown,unverified` e modo offline `--no-verification`.

## Fontes
- [TruffleHog GitHub — README.md (4 Pillars: Discovery, Classification, Validation & Analysis, --results Filters, CI/CD & Custom Detectors)](https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/README.md) — README oficial do trufflesecurity/trufflehog documentando os 4 pilares, verificação ativa de credenciais, exit code 183 com --fail, verificação Cosign e detectores customizados; consultado em 2026-10-03.
- [TruffleHog GitHub — CONTRIBUTING.md (Architecture of Pipeline Stages, Aho-Corasick Keyword Matching, Detectors & Verification)](https://github.com/trufflesecurity/trufflehog/blob/main/CONTRIBUTING.md) — Guia técnico de arquitetura do TruffleHog detalhando o pipeline concorrente Source -> Chunker -> Matcher Aho-Corasick -> Detector -> Verifier -> Dispatcher; consultado em 2026-10-03.
- [TruffleHog — Official GitHub Repository (Truffle Security)](https://github.com/trufflesecurity/trufflehog) — Repositório oficial open-source do TruffleHog; consultado em 2026-10-03.
