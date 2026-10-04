---
id: software.seguranca.tranche17.001699
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
fontes: ["https://docs.github.com/en/code-security/concepts/supply-chain-security/dependabot-alerts", "https://github.com/advisories"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Correlacionar alertas Renovate com identificadores GHSA/CVE e advisory original

## Em uma frase
Alertas recebidos da plataforma podem carregar identificadores e referências que precisam ser preservados ao relacionar PR de atualização ao advisory original.

## Por que importa
Nomes de pacote e severidade isolados são ambíguos; IDs facilitam deduplicação, investigação e comunicação entre GitHub, scanner e registro interno.

## Como funciona
Quando o advisory fornece IDs GHSA/CVE e aliases, preserve cada identificador, URL primária, versões afetadas, dependência reversa e commit corrigido, sem tratar um alias como evidência independente.

## Exemplo
Se o alerta inclui GHSA e CVE, registre ambos como identificadores relacionados e confirme faixa afetada na fonte do advisory antes de encerrar.

## Limites e trade-offs
Fontes diferentes podem atualizar alias, severidade e ranges em momentos distintos; Renovate não elimina diferenças de taxonomia.

## Como verificar
Abra a URL do advisory, confirme IDs e versões, compare lockfile antes/depois e mantenha uma referência ao merge e deploy.

## Conexões
- [[renovate-config-validation-preview-dry-run]] — Validar configuração Renovate antes de ativar regras de segurança.
- [[renovate-vulnerabilityalerts-limitacoes-alertas-sem-patch]] — PR de vulnerabilidade sem patch disponível: registrar mitigação em vez de assumir correção.

## Fontes
- [GitHub Docs — Dependabot alerts](https://docs.github.com/en/code-security/concepts/supply-chain-security/dependabot-alerts) — identificadores, versões vulneráveis e referências exibidas em alertas; consultado em 2026-10-04.
- [GitHub Advisory Database](https://github.com/advisories) — advisories e aliases GHSA/CVE publicados pelo GitHub; consultado em 2026-10-04.
