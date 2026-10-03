---
id: software.devops.tranche04.000320
tipo: tecnica
dominio: software
subdominio: devops
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-devops-2000-0002-tranche-04.md"
fontes: ["https://raw.githubusercontent.com/longhorn/longhorn/master/README.md", "https://longhorn.io/docs/latest/", "https://github.com/longhorn/longhorn"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Coleta de Support Bundle para diagnóstico de bugs e reporte de vulnerabilidades no Longhorn

## Em uma frase
O README oficial do Longhorn estabelece o protocolo de diagnóstico e segurança da comunidade: ao abrir uma issue de bug em `github.com/longhorn/longhorn/issues/new/choose` (revisada semanalmente na reunião comunitária de triagem), o usuário deve gerar e anexar o **Support Bundle** do Longhorn (ou enviá-lo para `longhorn-support-bundle@suse.com` quando contiver dados sensíveis do ambiente), enquanto vulnerabilidades de segurança devem ser reportadas de forma privada para `longhorn-security@suse.com`.

## Por que importa
Problemas de armazenamento distribuído envolvem interações entre kernel do host, driver CSI, `longhorn-manager`, `instance-manager` e logs de engine. O Support Bundle consolida automaticamente os manifestos YAML dos CRDs do Longhorn, eventos do Kubernetes e logs dos componentes para permitir reprodução e análise precisa da causa-raiz.

## Como funciona
Sempre gere um Support Bundle através do Longhorn UI ou CLI no momento exato em que uma anomalia de volume ou falha de rebuild ocorrer, antes de reiniciar pods ou excluir recursos que apaguem as evidências de log.

## Exemplo
Ao enfrentar um travamento de desconexão de volume após perda abrupta de rede entre nós, o engenheiro gera o Support Bundle pelo painel do Longhorn, inspeciona os logs consolidados do `longhorn-manager` e `instance-manager` e anexa o pacote sanitizado ao chamado técnico.

## Limites e trade-offs
Nunca publique credenciais de Backup Target S3 ou dados confidenciais em issues públicas do GitHub; revise o conteúdo ou envie o Support Bundle diretamente para o canal privado indicado pela documentação oficial.

## Como verificar
Gere um Support Bundle de teste em ambiente de homologação pelo painel do Longhorn e confirme que o arquivo compactado contém os logs dos componentes e o dump dos CRDs de `longhorn-system`.

## Conexões
- [[longhorn-ui-dashboard-and-cli-operations]] — Veja também: Operação visual e por linha de comando com Longhorn UI e Longhorn CLI.

## Fontes
- [Longhorn GitHub — README.md (Architecture, Features, Releases, Components & Libraries)](https://raw.githubusercontent.com/longhorn/longhorn/master/README.md) — README oficial do projeto CNCF Incubating Longhorn descrevendo a arquitetura de controlador dedicado por volume e réplicas síncronas em contêineres, recursos corporativos, matriz de releases ativas (1.11, 1.12, 1.13) e tabela completa de componentes e bibliotecas (Engine V1 iSCSI e V2 SPDK).; consultado em 2026-10-03.
- [Longhorn — Official Documentation (Deploy, Architecture & Concepts)](https://longhorn.io/docs/latest/) — Documentação oficial do Longhorn detalhando requisitos de instalação via kubectl, Helm e Rancher, replicação síncrona, snapshots incrementais, backups em NFSv4/S3 e upgrades não disruptivos.; consultado em 2026-10-03.
- [Longhorn — Official GitHub Repository](https://github.com/longhorn/longhorn) — Repositório principal Apache-2.0 do Longhorn na CNCF.; consultado em 2026-10-03.
