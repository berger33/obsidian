---
id: software.seguranca.tranche11.001062
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

# Catálogo dos **27+ Plugins Detectores** do `detect-secrets`: `AWSKeyDetector`, `OpenAIDetector`, `GitHubTokenDetector`, `KeywordDetector` e Limiares de Entropia

## Em uma frase
Como o `detect-secrets` identifica diferentes classes de credenciais sem exigir que você escreva expressões regulares do zero? Através de sua arquitetura modular de **Plugins Detectores (`detect-secrets scan --list-all-plugins`)**!

## Por que importa
Conforme listado na documentação oficial, o `detect-secrets` traz habilitados por padrão mais de **27 detectores especializados**: **(1) Provedores Cloud & Infraestrutura**: `AWSKeyDetector`, `AzureStorageKeyDetector`, `IbmCloudIamDetector`, `IbmCosHmacDetector`, `SoftlayerDetector`, `ArtifactoryDetector`; **(2) Código, IA & Pacotes**: `GitHubTokenDetector`, `GitLabTokenDetector`, `NpmDetector`, `PypiTokenDetector`, **`OpenAIDetector`**; **(3) SaaS, Pagamentos & Mensageria**: `StripeDetector`, `SquareOAuthDetector`, `TwilioKeyDetector`, `SendGridDetector`, `MailchimpDetector`, `SlackDetector`, `DiscordBotTokenDetector`, `TelegramBotTokenDetector`, `CloudantDetector`; e **(4) Detectores Genéricos & Heurísticos**: `PrivateKeyDetector`, `JwtTokenDetector`, `BasicAuthDetector`, `IPPublicDetector`, **`KeywordDetector`**, **`Base64HighEntropyString`** e **`HexHighEntropyString`**!

## Como funciona
Você pode calibrar a sensibilidade de entropia de Shannon com **`--base64-limit` (padrão `4.5`, escala `0.0–8.0`)** e **`--hex-limit` (padrão `3.0`)**, ou desativar plugins específicos com **`--disable-plugin`**!

## Exemplo
```bash
# Listar todos os plugins detectores disponiveis e calibrar os limiares de entropia Base64 e Hex ao gerar o baseline
detect-secrets scan --list-all-plugins
detect-secrets scan \
  --base64-limit 4.5 \
  --hex-limit 3.0 \
  --disable-plugin IPPublicDetector > .secrets.baseline
```

## Limites e trade-offs
Para testar rapidamente no terminal se uma string isolada (como um token de exemplo que você pretende colocar em um teste unitário) dispara algum dos 27 detectores e qual é a entropia exata calculada por `Base64HighEntropyString` / `HexHighEntropyString`, use a flag **`--string`**: `detect-secrets scan --string "minha_string_suspeita_aqui"`!

## Como verificar
Observe que todas as configurações de plugins e limiares passadas no `detect-secrets scan` ficam gravadas na chave `"plugins_used"` dentro do próprio arquivo `.secrets.baseline`, garantindo que o `detect-secrets-hook` aplique exatamente a mesma política.

## Conexões
- [[detectsecrets-arquitetura-baseline-separacao-responsabilidades-yelp]] — Veja também: **Yelp `detect-secrets` (`Yelp/detect-secrets`)**: Arquitetura de **Separação de Responsabilidades (`Separation of Concerns`)** e Arquivo **`.secrets.baseline`**.
- [[detectsecrets-fluxo-auditoria-interativa-audit-rotulacao-verificacao]] — Veja também: Auditoria Interativa e Verificação Ativa com **`detect-secrets audit`**: Rotulação (`is_secret`), Relatório (`--report`) e Comparação (**`--diff`**).
- [[detectsecrets-sistema-filtros-heuristicos-custom-filters-allowlist]] — Referência cruzada direta com detectsecrets-sistema-filtros-heuristicos-custom-filters-allowlist.

## Fontes
- [Yelp `detect-secrets` Official GitHub — Enterprise Secret Detection, `.secrets.baseline`, Plugins & Filters](https://raw.githubusercontent.com/Yelp/detect-secrets/master/README.md) — documentação oficial do `detect-secrets` cobrindo `scan`, `audit`, `detect-secrets-hook`, os 27+ plugins detectores, filtros heurísticos e API Python `SecretsCollection`; consultado em 2026-10-03.
- [Yelp `detect-secrets` Official Pre-Commit Hook Specification (`.pre-commit-hooks.yaml`)](https://raw.githubusercontent.com/Yelp/detect-secrets/master/.pre-commit-hooks.yaml) — especificação oficial do hook `detect-secrets-hook` para integração em pipelines e estações de desenvolvimento; consultado em 2026-10-03.
