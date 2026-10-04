---
id: software.seguranca.tranche17.001695
tipo: tecnica
dominio: software
subdominio: seguranca
nivel: intermediario
confianca: media
ultima_verificacao: 2026-10-04
validade: volatil
status: candidata
revisao_humana: nao_solicitada
revisor: ""
revisao_ia: aprovada
revisor_ia: "Arena.ai Agent Mode"
data_revisao_ia: 2026-10-04
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-17.md"
fontes: ["https://docs.renovatebot.com/presets-security/", "https://docs.renovatebot.com/config-overview/#inherited-config"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Aplicar presets de segurança Renovate com configuração herdada revisável

## Em uma frase
Os presets de segurança oferecem configurações reutilizáveis para regras relacionadas a vulnerabilidades, dependências ou políticas de atualização.

## Por que importa
Um preset compartilhado evita divergência entre dezenas de repositórios, mas mudanças upstream podem alterar comportamento herdado sem edição local.

## Como funciona
Fixe referência do preset quando política exigir estabilidade, valide a configuração final e documente quais opções locais substituem defaults herdados.

## Exemplo
Um repositório pode estender um preset aprovado e rodar o validador de configuração em pull request sempre que o preset mudar.

```text
renovate-config-validator
```

## Limites e trade-offs
Preset é conveniência de configuração, não atestado de que Dependency Graph, permissões e alertas estão corretamente ativados.

## Como verificar
Expanda configuração final, confira logs de Renovate e confirme que PRs de teste seguem as regras esperadas.

## Conexões
- [[renovate-osv-vulnerability-alerts-experimental-escopo]] — `osvVulnerabilityAlerts` no Renovate: recurso marcado experimental e sujeito a validação.
- [[renovate-vulnerabilityalerts-github-permissions-self-hosted]] — Permissões e execução self-hosted para alertas de vulnerabilidade Renovate.

## Fontes
- [Renovate — Security Presets](https://docs.renovatebot.com/presets-security/) — presets e políticas de atualização de segurança reutilizáveis; consultado em 2026-10-04.
- [Renovate — Configuration Overview](https://docs.renovatebot.com/config-overview/#inherited-config) — herança, extensão e composição da configuração efetiva; consultado em 2026-10-04.
