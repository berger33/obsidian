---
id: software.seguranca.tranche14.001372
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-14.md"
fontes: ["https://raw.githubusercontent.com/gravitational/teleport/master/README.md", "https://goteleport.com/docs/reference/architecture/"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Acesso SSH com **Gravação Completa de Sessão Interativa** e **Auditoria Enriquecida por eBPF (`enhanced_recording`)** no Teleport

## Em uma frase
O que acontece se um engenheiro ou terceiro autorizado acessar um servidor Linux via SSH e, em vez de digitar comandos em texto claro no terminal (que apareceriam na gravação de tela TTY), ele executar um script obscuro `curl ... | bash`, rodar um binário codificado em Base64 ou abrir um sub-shell que limpa o histórico?

## Por que importa
Um gravador de terminal comum veria apenas `./script.sh` na tela, sem saber quais binários foram executados por baixo nem quais conexões de rede o script abriu!

## Como funciona
O **Teleport SSH Service** resolve ambos os problemas: além de gravar a **sessão interativa completa de terminal TTY** (que pode ser assistida como um vídeo no navegador ou via `tsh play <session-id>`!), ele inclui a **Gravação Aprimorada Baseada em eBPF (`enhanced_recording: enabled: true`)**! Usando programas **eBPF** acoplados aos *tracepoints* do Kernel Linux ligados ao `cgroup` da sessão SSH, o Teleport registra no log de auditoria estruturado **cada chamada `execve` (`session.command`), cada arquivo aberto (`session.disk`) e cada conexão TCP de rede (`session.network`)** disparada dentro daquela sessão SSH!

## Exemplo
```yaml
# Habilitar no /etc/teleport.yaml do agente SSH a gravacao de sessao e o rastreamento de execucao/rede via eBPF (enhanced_recording)
version: v3
ssh_service:
  enabled: "yes"
  labels:
    env: producao
    tier: backend
  enhanced_recording:
    enabled: true
    command_buffer_size: 8
    disk_buffer_size: 128
    network_buffer_size: 8
```

## Limites e trade-offs
E se você tiver servidores Linux ou equipamentos onde não deseja instalar o agente `teleport`, mas que já rodam o **`sshd` padrão do OpenSSH**? O Teleport também suporta nodes **OpenSSH Agentless**: basta configurar **`TrustedUserCAKeys`** no `/etc/ssh/sshd_config` apontando para a chave pública da CA de usuários do Teleport (`tctl auth export --type=user`)!

## Como verificar
Para operações de altíssima criticidade em produção, o Teleport permite inclusive configurar políticas de **`Moderated Sessions` (*Four-Eyes Principle*)**: a sessão SSH do engenheiro só destrava o teclado quando um segundo revisor autorizado entra ao vivo na mesma sessão com sua chave FIDO2 WebAuthn para acompanhar a operação!

## Conexões
- [[teleport-arquitetura-zero-trust-auth-proxy-agents-certificados-curtos]] — Veja também: Arquitetura do **Gravitational Teleport (`gravitational/teleport`)**: Acesso **Zero-Trust Baseado em Identidade** e **Certificados de Curta Duração** (Sem Chaves Estáticas!).
- [[teleport-acesso-kubernetes-databases-mtls-impersonation-sem-senhas]] — Veja também: Acesso Zero-Trust a **Clusters Kubernetes (`tsh kube login`)** e **Bancos de Dados (`tsh db connect` — PostgreSQL, MySQL, MongoDB, Redis)** sem Senhas Compartilhadas.
- [[teleport-rbac-abac-labels-roles-per-session-mfa-fido2-webauthn]] — Referência cruzada direta com teleport-rbac-abac-labels-roles-per-session-mfa-fido2-webauthn.
- [[teleport-auditoria-eventos-gravacao-s3-dynamodb-integracao-siem]] — Referência cruzada direta com teleport-auditoria-eventos-gravacao-s3-dynamodb-integracao-siem.

## Fontes
- [Gravitational Teleport Official GitHub Repository (`gravitational/teleport`)](https://raw.githubusercontent.com/gravitational/teleport/master/README.md) — repositório oficial do Teleport cobrindo acesso Zero-Trust sem chaves estáticas para SSH, Kubernetes, Databases, Web Apps, Windows Desktops e MCP com RBAC/ABAC e JIT Access Requests; consultado em 2026-10-03.
- [Teleport Official Architecture Reference (`goteleport.com/docs/reference/architecture`)](https://goteleport.com/docs/reference/architecture/) — documentação oficial de arquitetura do Teleport detalhando `Auth Service` (CA e auditoria), `Proxy Service` (reverse tunnels e TLS routing), `Agents`, `Machine ID` (`tbot`), `Node Joining` (IAM/TPM) e `Trusted Clusters`; consultado em 2026-10-03.
