---
id: software.seguranca.tranche10.000968
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-10.md"
fontes: ["https://raw.githubusercontent.com/thoughtworks/talisman/main/README.md", "https://raw.githubusercontent.com/thoughtworks/talisman/main/.pre-commit-hooks.yaml"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Governança DevSecOps sobre o `.talismanrc`: Como Impedir que Desenvolvedores Aprovem Vazamentos Reais via **GitHub `CODEOWNERS`** e Auditoria de PR

## Em uma frase
Pense como um engenheiro de AppSec: se qualquer desenvolvedor puder usar `talisman -i` para adicionar um arquivo que contém uma chave privada real ao `.talismanrc` e fazer o commit da chave junto com o `.talismanrc` atualizado, o hook local passará!

## Por que importa
Como fechar essa brecha de governança no fluxo de Pull Requests da empresa? Combinando duas barreiras no servidor Git (GitHub / GitLab): **(1) Proteger o arquivo `.talismanrc` no arquivo `.github/CODEOWNERS`** atribuindo sua propriedade exclusiva ao time `@org/appsec-team` (com Branch Protection exigindo `Require review from Code Owners`); e **(2) Executar um passo de auditoria no CI/CD que verifica especificamente se o PR modificou o `.talismanrc`**!

## Como funciona
Com `.talismanrc @org/appsec-team` no `CODEOWNERS`, um desenvolvedor ainda pode aprovar um falso positivo localmente para continuar trabalhando na sua branch, mas **o Pull Request só poderá ser mesclado na `main` após um engenheiro de segurança revisar o diff do `.talismanrc` e confirmar que o arquivo ignorado realmente é um falso positivo**!

## Exemplo
```bash
# Em um job de CI/CD de Pull Request: verificar se o .talismanrc foi modificado e listar os arquivos ignorados para revisao de seguranca
git diff --name-only origin/main...HEAD | grep -qx "\.talismanrc" && {
  echo "[ALERTA APPSEC] O arquivo .talismanrc foi alterado neste PR! Inspecionando entradas:"
  git diff origin/main...HEAD -- .talismanrc
}
talisman --githook pre-push
```

## Limites e trade-offs
Essa arquitetura **"Self-Service Local com Governança Centralizada no Merge"** é o equilíbrio perfeito de DevSecOps: zero bloqueio burocrático enquanto o desenvolvedor codifica na branch local, e 100% de garantia de auditoria antes do código entrar na branch principal!

## Como verificar
Complemente a execução de `talisman --githook pre-push` no CI/CD com a verificação ativa de credenciais do **TruffleHog (`--only-verified`)**.

## Conexões
- [[talisman-anatomia-detectores-entropia-base64-hex-creditcard-filesize]] — Veja também: Por Dentro dos Detectores do Talisman: Cálculo de **Entropia de Shannon**, Decodificação Recursiva **Base64/Hex**, Cartões de Crédito e Limite de Tamanho.
- [[talisman-resposta-incidente-vazamento-revogacao-git-filter-repo]] — Veja também: Resposta a Incidentes de Vazamento de Segredo no Git: Por Que um Commit de `git rm` Não Apaga o Segredo e Como Limpar o Histórico com `git filter-repo`.
- [[talisman-governanca-checksum-sha256-talismanrc-ignore-detectors]] — Referência cruzada direta com talisman-governanca-checksum-sha256-talismanrc-ignore-detectors.
- [[steampipe-auditoria-postura-github-supply-chain-branch-protection-actions]] — Referência cruzada direta com steampipe-auditoria-postura-github-supply-chain-branch-protection-actions.

## Fontes
- [Thoughtworks Talisman Official GitHub — Secret Detection in Git Hooks, `.talismanrc` SHA-256 Checksums, Detectors & History Scanner](https://raw.githubusercontent.com/thoughtworks/talisman/main/README.md) — documentação oficial do Talisman cobrindo os 6 detectores de validação, configuração `.talismanrc` por checksum SHA-256, `scopeconfig`, modo interativo e `--scan`; consultado em 2026-10-03.
- [Thoughtworks Talisman Official Pre-Commit Hooks Specification (`.pre-commit-hooks.yaml`)](https://raw.githubusercontent.com/thoughtworks/talisman/main/.pre-commit-hooks.yaml) — especificação oficial dos hooks `talisman-commit` e `talisman-push` em Go; consultado em 2026-10-03.
