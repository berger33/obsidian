---
id: software.seguranca.tranche11.001061
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-11.md"
fontes: ["https://raw.githubusercontent.com/Yelp/detect-secrets/master/README.md", "https://raw.githubusercontent.com/Yelp/detect-secrets/master/.pre-commit-hooks.yaml"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# **Yelp `detect-secrets` (`Yelp/detect-secrets`)**: Arquitetura de **Separação de Responsabilidades (`Separation of Concerns`)** e Arquivo **`.secrets.baseline`**

## Em uma frase
Criado pela equipe de Engenharia de Segurança do **Yelp** (`Yelp/detect-secrets`, escrito em Python 3), o **`detect-secrets`** foi projetado especificamente para resolver o maior obstáculo de adoção de scanners de segredos em **grandes empresas e monorepos legados com milhões de linhas de código**: *como ativar um bloqueador de commits hoje de manhã em 1.000 repositórios antigos sem quebrar o build por causa dos 500 falsos positivos ou segredos legados que já estavam no código há anos?*!

## Por que importa
Conforme explica o `README.md` oficial, o `detect-secrets` aplica o princípio de **Separação de Responsabilidades (*Separation of Concerns*)** através do arquivo JSON **`.secrets.baseline`** e de três ferramentas complementares: **(1) `detect-secrets scan`** — fotografia todos os possíveis segredos que *já existem hoje* no repositório e salva seus hashes SHA-1 no `.secrets.baseline`; **(2) `detect-secrets-hook`** — roda no `pre-commit` / CI analisando apenas os arquivos modificados (`git diff --staged`) e **bloqueia estritamente qualquer segredo NOVO que não esteja registrado no `.secrets.baseline`**;

## Como funciona
e **(3) `detect-secrets audit`** — permite ao time de segurança auditar, rotular e migrar os itens do baseline no seu próprio ritmo sem travar os desenvolvedores!

## Exemplo
```bash
# Instalar o detect-secrets, gerar o arquivo inicial .secrets.baseline na raiz do repositorio e atualizar um baseline existente
pip install detect-secrets
detect-secrets scan > .secrets.baseline
detect-secrets scan --baseline .secrets.baseline
```

## Limites e trade-offs
Entenda por que o comando **`detect-secrets scan --baseline .secrets.baseline`** é tão prático na manutenção do repositório: ao reescanear o código contra um baseline existente, ele atualiza o formato do JSON, remove automaticamente segredos que já foram apagados do código e **preserva intactos todos os rótulos (`is_secret: true/false`) que o time de segurança já auditou anteriormente**!

## Como verificar
Nunca salve segredos em texto claro no baseline: o `.secrets.baseline` armazena apenas o **`hashed_secret` (SHA-1)**, o nome do arquivo, o número da linha e o plugin detector.

## Conexões
- [[detectsecrets-plugins-detectores-entropia-base64-hex-keyword-cloud]] — Veja também: Catálogo dos **27+ Plugins Detectores** do `detect-secrets`: `AWSKeyDetector`, `OpenAIDetector`, `GitHubTokenDetector`, `KeywordDetector` e Limiares de Entropia.
- [[detectsecrets-fluxo-auditoria-interativa-audit-rotulacao-verificacao]] — Referência cruzada direta com detectsecrets-fluxo-auditoria-interativa-audit-rotulacao-verificacao.
- [[talisman-comparacao-talisman-vs-git-secrets-vs-gitleaks-vs-trufflehog]] — Referência cruzada direta com talisman-comparacao-talisman-vs-git-secrets-vs-gitleaks-vs-trufflehog.

## Fontes
- [Yelp `detect-secrets` Official GitHub — Enterprise Secret Detection, `.secrets.baseline`, Plugins & Filters](https://raw.githubusercontent.com/Yelp/detect-secrets/master/README.md) — documentação oficial do `detect-secrets` cobrindo `scan`, `audit`, `detect-secrets-hook`, os 27+ plugins detectores, filtros heurísticos e API Python `SecretsCollection`; consultado em 2026-10-03.
- [Yelp `detect-secrets` Official Pre-Commit Hook Specification (`.pre-commit-hooks.yaml`)](https://raw.githubusercontent.com/Yelp/detect-secrets/master/.pre-commit-hooks.yaml) — especificação oficial do hook `detect-secrets-hook` para integração em pipelines e estações de desenvolvimento; consultado em 2026-10-03.
