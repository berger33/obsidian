---
id: software.seguranca.tranche11.001070
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

# Estratégia de Adoção Corporativa (`Brownfield` vs `Greenfield`): Combinando **Yelp `detect-secrets`**, **Talisman**, **`git-secrets`**, **Gitleaks** e **TruffleHog**

## Em uma frase
Com o estudo do **`detect-secrets`**, completamos o quarteto de ferramentas de prevenção de vazamento de segredos em Git ao lado de **Thoughtworks Talisman**, **awslabs `git-secrets`**, **Gitleaks** e **TruffleHog**. Como desenhar uma estratégia de implantação corporativa para **500+ repositórios** sem paralisar a engenharia?

## Por que importa
Divida seus repositórios em duas categorias: **(1) Repositórios `Greenfield` (Novos ou já limpos)**: já nascem com baseline zero; use **`detect-secrets`**, **Gitleaks** ou **Talisman** bloqueando 100% de qualquer achado no `pre-commit` e no CI!

## Como funciona
E **(2) Repositórios `Brownfield` (Monorepos legados gigantescos com dívida técnica acumulada)**: no **Dia 1**, rode `detect-secrets scan --slim > .secrets.baseline` e ative o **`detect-secrets-hook`** no `pre-commit` e no CI — **estancando o sangramento em 100% para novos commits no mesmo dia sem quebrar uma única build legada**! Em seguida, nas semanas seguintes, o time de AppSec roda **`detect-secrets audit .secrets.baseline`** e **`trufflehog git --only-verified`** para rotacionar apenas as credenciais ativas reais herdadas do passado!

## Exemplo
```bash
# Dia 1 de implantacao Brownfield em um repositorio legado: gerar o baseline slim e validar que o hook passa imediatamente com codigo 0
detect-secrets scan --slim > .secrets.baseline
git diff --staged --name-only -z | xargs -0 detect-secrets-hook --baseline .secrets.baseline
echo "Status do hook sobre os arquivos em stage: $?"
```

## Limites e trade-offs
Essa estratégia em duas fases (*Dia 1: Estancar novos segredos com `.secrets.baseline` -> Fase 2: Drenar o legado com `detect-secrets audit` + `trufflehog --only-verified`*) é o padrão adotado pelas maiores equipes de DevSecOps do mundo porque entrega proteção imediata em 24 horas sem exigir semanas de limpeza prévia.

## Como verificar
À medida que as dívidas do `.secrets.baseline` forem sendo migradas para o Vault/Secrets Manager e removidas do código, o comando `detect-secrets scan --baseline .secrets.baseline` vai encolhendo automaticamente o arquivo até zerar.

## Conexões
- [[detectsecrets-calibracao-keyworddetector-falsos-positivos-testes-i18n]] — Veja também: Afundando Falsos Positivos do **`KeywordDetector`** no `detect-secrets`: Como Escrever Código e Testes Sem Disparar Alertas de Variáveis `password` / `secret` / `token`.
- [[detectsecrets-arquitetura-baseline-separacao-responsabilidades-yelp]] — Referência cruzada direta com detectsecrets-arquitetura-baseline-separacao-responsabilidades-yelp.
- [[detectsecrets-fluxo-auditoria-interativa-audit-rotulacao-verificacao]] — Referência cruzada direta com detectsecrets-fluxo-auditoria-interativa-audit-rotulacao-verificacao.
- [[talisman-comparacao-talisman-vs-git-secrets-vs-gitleaks-vs-trufflehog]] — Referência cruzada direta com talisman-comparacao-talisman-vs-git-secrets-vs-gitleaks-vs-trufflehog.

## Fontes
- [Yelp `detect-secrets` Official GitHub — Enterprise Secret Detection, `.secrets.baseline`, Plugins & Filters](https://raw.githubusercontent.com/Yelp/detect-secrets/master/README.md) — documentação oficial do `detect-secrets` cobrindo `scan`, `audit`, `detect-secrets-hook`, os 27+ plugins detectores, filtros heurísticos e API Python `SecretsCollection`; consultado em 2026-10-03.
- [Yelp `detect-secrets` Official Pre-Commit Hook Specification (`.pre-commit-hooks.yaml`)](https://raw.githubusercontent.com/Yelp/detect-secrets/master/.pre-commit-hooks.yaml) — especificação oficial do hook `detect-secrets-hook` para integração em pipelines e estações de desenvolvimento; consultado em 2026-10-03.
