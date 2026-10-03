---
id: software.devops.tranche04.000377
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
fontes: ["https://raw.githubusercontent.com/cri-o/cri-o/main/README.md", "https://cri-o.github.io/cri-o", "https://github.com/cri-o/cri-o"]
tags: [dominio/software, subdominio/devops, qualidade/candidata]
lote: software-devops-2000-0002
---

# Suporte a OCI Hooks e guia de migração de anotações no CRI-O

## Em uma frase
O README oficial documenta que o CRI-O pode ser configurado para injetar **OCI Hooks** (`spec-hooks` da especificação POSIX do runtime OCI) ao criar contêineres, permitindo executar ações customizadas no host em estágios específicos do ciclo de vida do contêiner (como `prestart`, `createRuntime`, `poststart` e `poststop`). Além disso, o projeto mantém o **Annotation Migration Guide** (`ANNOTATION_MIGRATION.md`), orientando a migração de anotações específicas do CRI-O para as convenções de nomenclatura recomendadas pelo Kubernetes.

## Por que importa
Cargas especializadas — como injeção de dispositivos de GPU, ajustes de rede de baixa latência ou agentes de segurança e auditoria — frequentemente dependem de OCI Hooks configurados em arquivos JSON no nó e de anotações específicas nos pods para ativar comportamentos do runtime.

## Como funciona
Configure diretórios de OCI Hooks (`hooks_dir` no `crio.conf`) com filtros precisos de anotação ou comando para que o hook seja disparado apenas nos contêineres que realmente necessitam da preparação customizada, e siga `ANNOTATION_MIGRATION.md` ao atualizar manifestos antigos.

## Exemplo
Para habilitar preparação automática de dispositivos aceleradores em pods de inferência sem conceder `privileged: true`, a equipe instala o OCI Hook correspondente no diretório monitorado pelo CRI-O, ativado apenas quando o pod apresenta a anotação esperada.

## Limites e trade-offs
Um OCI Hook com erro ou que demora para retornar bloqueia a inicialização do contêiner no Kubelet; mantenha scripts/binários de hooks enxutos, idempotentes e com tratamento estrito de timeout.

## Como verificar
Inspecione a configuração de `hooks_dir` via `sudo crio status config` e verifique a execução do hook apenas nos pods marcados com a anotação correspondente.

## Conexões
- [[crio-signature-verification-policy-json-enforcement]] — Veja também: Verificação nativa de assinaturas de imagem no nó Kubernetes com policy.json no CRI-O.
- [[crio-running-kubernetes-with-crio-socket-and-systemd]] — Veja também: Configuração do Kubelet com CRI-O via endpoint unix:///var/run/crio/crio.sock e systemd cgroup.

## Fontes
- [CRI-O GitHub — README.md (Kubernetes Compatibility Matrix, Scope, Config & HTTP Status API)](https://raw.githubusercontent.com/cri-o/cri-o/main/README.md) — README oficial do CRI-O detalhando alinhamento de versões 1.x.y e política de version skew n-2 com o Kubernetes, escopo estrito de implementação da CRI para o Kubelet, bibliotecas OCI (runc, container-libs/image, container-libs/storage, CNI), arquivos crio.conf, policy.json, registries.conf, storage.conf e API de status via crio status e socket /var/run/crio/crio.sock.; consultado em 2026-10-03.
- [CRI-O — Official Release Notes & Documentation Portal](https://cri-o.github.io/cri-o) — Portal oficial de notas de versão e relatórios de dependências do CRI-O mantido pelos desenvolvedores do projeto.; consultado em 2026-10-03.
- [CRI-O — Official GitHub Repository](https://github.com/cri-o/cri-o) — Repositório oficial Apache-2.0 do CRI-O na CNCF.; consultado em 2026-10-03.
