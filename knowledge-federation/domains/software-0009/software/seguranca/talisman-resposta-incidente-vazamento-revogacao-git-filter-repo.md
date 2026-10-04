---
id: software.seguranca.tranche10.000969
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

# Resposta a Incidentes de Vazamento de Segredo no Git: Por Que um Commit de `git rm` Não Apaga o Segredo e Como Limpar o Histórico com `git filter-repo`

## Em uma frase
O que fazer quando o `talisman --scan` descobre que uma chave privada `.pem` ou senha de banco de dados foi commitada 3 semanas atrás no repositório Git?

## Por que importa
O erro mais grave e comum é fazer apenas `git rm chave.pem && git commit -m "remove key" && git push`: isso remove o arquivo apenas do `HEAD` atual, mas **o blob contendo a chave privada continua 100% acessível para qualquer pessoa que tenha acesso de leitura ao repositório através de `git log -p` ou `git show <commit_antigo>`**!

## Como funciona
O protocolo obrigatório de resposta a incidentes de segredos expostos em Git exige **duas ações na ordem exata**: **(1) PRIMEIRO: Revogar e Rotacionar Imediatamente a Credencial no Provedor** (assumindo que qualquer segredo que tocou um repositório remoto já foi copiado por bots/clones); e **(2) SEGUNDO: Expurgar o blob de todos os commits, branches e tags do histórico Git usando `git filter-repo --invert-paths --path <arquivo>` (ou `--replace-text`)** e re-executar `talisman --scan` para provar que o histórico está limpo!

## Exemplo
```bash
# Passo 1 (Apos revogar a chave no provedor!): expurgar completamente um arquivo sensivel de todo o historico Git e validar com Talisman
git filter-repo --invert-paths --path certs/leaked-private.key --force
talisman --scan --reportdirectory=/cases/appsec/post_cleanup_verification
jq '.results | length' /cases/appsec/post_cleanup_verification/data/report.json
```

## Limites e trade-offs
Atenção após reescrever o histórico no servidor Git: os objetos órfãos antigos ainda podem permanecer acessíveis por 30–90 dias via cache de Pull Requests ou `reflog` no GitHub/GitLab se o hash do commit for conhecido; por isso, **a expurgação do histórico Git NUNCA substitui a revogação imediata da chave**!

## Como verificar
Após o `git filter-repo`, confirme que `jq '.results | length'` no relatório do `talisman --scan` retorna `0`.

## Conexões
- [[talisman-auditoria-seguranca-talismanrc-codeowners-bypass-detection]] — Veja também: Governança DevSecOps sobre o `.talismanrc`: Como Impedir que Desenvolvedores Aprovem Vazamentos Reais via **GitHub `CODEOWNERS`** e Auditoria de PR.
- [[talisman-comparacao-talisman-vs-git-secrets-vs-gitleaks-vs-trufflehog]] — Veja também: Defesa em Profundidade para Segredos no Git: Comparação Técnica entre **Talisman**, **`git-secrets`**, **Gitleaks** e **TruffleHog**.
- [[talisman-varredura-historico-git-scan-reportdirectory-scanwithhtml]] — Referência cruzada direta com talisman-varredura-historico-git-scan-reportdirectory-scanwithhtml.

## Fontes
- [Thoughtworks Talisman Official GitHub — Secret Detection in Git Hooks, `.talismanrc` SHA-256 Checksums, Detectors & History Scanner](https://raw.githubusercontent.com/thoughtworks/talisman/main/README.md) — documentação oficial do Talisman cobrindo os 6 detectores de validação, configuração `.talismanrc` por checksum SHA-256, `scopeconfig`, modo interativo e `--scan`; consultado em 2026-10-03.
- [Thoughtworks Talisman Official Pre-Commit Hooks Specification (`.pre-commit-hooks.yaml`)](https://raw.githubusercontent.com/thoughtworks/talisman/main/.pre-commit-hooks.yaml) — especificação oficial dos hooks `talisman-commit` e `talisman-push` em Go; consultado em 2026-10-03.
