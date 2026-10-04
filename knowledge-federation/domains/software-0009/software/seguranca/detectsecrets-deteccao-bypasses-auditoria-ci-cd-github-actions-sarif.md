---
id: software.seguranca.tranche11.001068
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

# Detecção de Bypass (`git commit --no-verify`) no CI/CD com `detect-secrets`: Como Auditar tanto **Novos Segredos** quanto **Adições Não-Auditadas ao Baseline**

## Em uma frase
O `README.md` oficial do `detect-secrets` destaca que um dos três pilares da ferramenta é **"Detectar se as prevenções locais foram explicitamente contornadas"**!

## Por que importa
Considere os dois jeitos pelos quais um desenvolvedor apressado pode tentar burlar o hook local do `detect-secrets`: **(1) Bypass por `--no-verify`**: ele roda `git commit --no-verify` e sobe um segredo novo no código sem atualizar o `.secrets.baseline`; ou **(2) Bypass por "Atualização Preguiçosa do Baseline"**: o hook bloqueia o commit, e o desenvolvedor roda `detect-secrets scan --baseline .secrets.baseline` para cadastrar o seu segredo real dentro do `.secrets.baseline` e fazer o hook calar a boca!

## Como funciona
Como barrar **ambos** os vetores no seu pipeline de **GitHub Actions / GitLab CI**? **(1)** Rode `git ls-files -z | xargs -0 detect-secrets-hook --baseline .secrets.baseline` no CI (barra qualquer segredo fora do baseline ou marcado como `"is_secret": true`); e **(2)** Exija que toda entrada presente no `.secrets.baseline` tenha sido **explicitamente auditada e rotulada (`"is_secret": false`)**!

## Exemplo
```bash
# No pipeline de CI/CD: (1) Rodar o detect-secrets-hook em todos os arquivos e (2) Falhar se houver entradas nao-auditadas ou reais no baseline!
git ls-files -z | xargs -0 detect-secrets-hook --baseline .secrets.baseline

jq -e '[.results[][] | select(.is_secret != false)] | length == 0' .secrets.baseline || {
  echo "ERRO: O .secrets.baseline contem segredos reais (is_secret: true) ou itens nao auditados via 'detect-secrets audit'!"
  exit 1
}
```

## Limites e trade-offs
Olhe a genialidade da validação com `jq -e '[.results[][] | select(.is_secret != false)] | length == 0' .secrets.baseline` acima: quando alguém roda apenas `detect-secrets scan --baseline .secrets.baseline`, os novos itens entram no JSON **sem o campo `"is_secret"`** (pois só o `detect-secrets audit` adiciona `"is_secret": false`!). Assim, combinando essa checagem `jq` com a proteção do `.secrets.baseline` no `.github/CODEOWNERS`, nenhum desenvolvedor consegue aprovar um segredo novo sozinho!

## Como verificar
Essa dupla checagem leva menos de 2 segundos para executar em qualquer runner de CI/CD.

## Conexões
- [[detectsecrets-modo-slim-resolucao-conflitos-merge-monorepos-escala]] — Veja também: Operando `detect-secrets` em **Monorepos de Grande Escala**: Modo **`--slim`**, Execução Paralela Multi-Core e Varredura de Arquivos Não-Rastreados (`--all-files`).
- [[detectsecrets-calibracao-keyworddetector-falsos-positivos-testes-i18n]] — Veja também: Afundando Falsos Positivos do **`KeywordDetector`** no `detect-secrets`: Como Escrever Código e Testes Sem Disparar Alertas de Variáveis `password` / `secret` / `token`.
- [[detectsecrets-arquitetura-baseline-separacao-responsabilidades-yelp]] — Referência cruzada direta com detectsecrets-arquitetura-baseline-separacao-responsabilidades-yelp.
- [[detectsecrets-fluxo-auditoria-interativa-audit-rotulacao-verificacao]] — Referência cruzada direta com detectsecrets-fluxo-auditoria-interativa-audit-rotulacao-verificacao.
- [[talisman-auditoria-seguranca-talismanrc-codeowners-bypass-detection]] — Referência cruzada direta com talisman-auditoria-seguranca-talismanrc-codeowners-bypass-detection.

## Fontes
- [Yelp `detect-secrets` Official GitHub — Enterprise Secret Detection, `.secrets.baseline`, Plugins & Filters](https://raw.githubusercontent.com/Yelp/detect-secrets/master/README.md) — documentação oficial do `detect-secrets` cobrindo `scan`, `audit`, `detect-secrets-hook`, os 27+ plugins detectores, filtros heurísticos e API Python `SecretsCollection`; consultado em 2026-10-03.
- [Yelp `detect-secrets` Official Pre-Commit Hook Specification (`.pre-commit-hooks.yaml`)](https://raw.githubusercontent.com/Yelp/detect-secrets/master/.pre-commit-hooks.yaml) — especificação oficial do hook `detect-secrets-hook` para integração em pipelines e estações de desenvolvimento; consultado em 2026-10-03.
