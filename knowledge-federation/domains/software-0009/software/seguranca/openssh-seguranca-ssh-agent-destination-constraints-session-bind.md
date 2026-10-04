---
id: software.seguranca.tranche12.001196
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-12.md"
fontes: ["https://raw.githubusercontent.com/openssh/openssh-portable/master/README", "https://www.openssh.com/releasenotes.html"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Segurança do **`ssh-agent`**: O Perigo do **`ForwardAgent yes`**, Restrições de Destino (**`ssh-add -h` + `session-bind@openssh.com`**) e Isolamento

## Em uma frase
Por que usar **`ForwardAgent yes`** (ou `ssh -A`) ao conectar em um servidor compartilhado ou máquina de bastion intermediária é considerado uma das práticas mais perigosas em administração Linux?

## Por que importa
Porque quando você faz *Agent Forwarding* tradicional para um servidor `host-intermediario`, o `sshd` cria um socket UNIX em `/tmp/ssh-XXXX/agent.<pid>` naquele servidor: **qualquer atacante que possua acesso `root` (ou consiga rodar código como o seu usuário) no `host-intermediario` pode conectar naquele socket e usar o seu `ssh-agent` local para se autenticar em TODOS os outros servidores e repositórios Git da empresa aos quais a sua chave tem acesso**, enquanto você estiver conectado!

## Como funciona
Como eliminar esse risco? Primeiro, **prefira sempre `ProxyJump` (`ssh -J bastion destino`) em vez de `ForwardAgent`** (pois no `ProxyJump` a autenticação ocorre de ponta a ponta entre a sua máquina e o destino final sem jamais expor o socket do agente no bastion!). E segundo, se você realmente precisar carregar uma chave no `ssh-agent` com restrição de onde ela pode ser usada, o OpenSSH 8.9+ / 10.5 suporta **Destination Constraints (`ssh-add -h`)** apoiadas pela extensão criptográfica **`session-bind@openssh.com`**!

## Exemplo
```bash
# Adicionar uma chave ao ssh-agent com tempo de vida maximo de 4h (-t 4h), exigindo confirmacao (-c) e restricao de salto de destino (-h)
ssh-add -t 4h -c \
  -h "bastion.corp.interno" \
  -h "bastion.corp.interno>db01.corp.interno" \
  ~/.ssh/id_ed25519_prod
```

## Limites e trade-offs
Como funciona a restrição **`-h "bastion.corp.interno>db01.corp.interno"`**? Graças à extensão **`session-bind@openssh.com`** (cujo bug de interação com bloqueio de agente foi corrigido no **OpenSSH 10.5**!), o cliente `ssh` registra criptograficamente no `ssh-agent` a identidade da chave de host de cada salto; se alguém no `bastion.corp.interno` tentar sequestrar o socket do agente para conectar em `cofre-secreto.corp.interno`, **o seu `ssh-agent` local recusa a assinatura porque o destino não está autorizado na cadeia `-h`**!

## Como verificar
Combine sempre `-t <tempo>` (expiração automática da chave na memória do agente) e `-c` (confirmação via `ssh-askpass` a cada uso) ao carregar chaves administrativas no `ssh-agent`.

## Conexões
- [[openssh-certificados-ssh-ca-user-host-certificates-principals-ttl]] — Veja também: Eliminando `authorized_keys` Estáticos e Alertas TOFU (`known_hosts`) com **Autoridade Certificadora SSH (`ssh-keygen -s` User & Host Certificates)**.
- [[openssh-tunelamento-seguro-proxyjump-bastion-restricao-forwarding]] — Veja também: Arquitetura de **Bastion Host (Jump Host)** com **`ProxyJump` (`-J`)** e Blindagem do Bastion com `AllowTcpForwarding local`, `PermitOpen` e `ForceCommand`.
- [[openssh-arquitetura-separacao-privilegios-sshd-session-sandbox-seccomp]] — Referência cruzada direta com openssh-arquitetura-separacao-privilegios-sshd-session-sandbox-seccomp.
- [[openssh-chaves-hardware-fido2-u2f-ed25519-sk-resident-keys-touch]] — Referência cruzada direta com openssh-chaves-hardware-fido2-u2f-ed25519-sk-resident-keys-touch.

## Fontes
- [OpenSSH Portable Official Repository README (`openssh/openssh-portable`)](https://raw.githubusercontent.com/openssh/openssh-portable/master/README) — documentação oficial do OpenSSH Portable detalhando a arquitetura derivada do OpenBSD, suporte a PAM/libcrypto e diretrizes de segurança; consultado em 2026-10-03.
- [OpenSSH Official Release Notes (OpenSSH 10.4 / 10.5p1)](https://www.openssh.com/releasenotes.html) — notas de lançamento oficiais do OpenSSH detalhando melhorias de segurança em `sshd-session`, `seccomp`/`NO_NEW_PRIVS` fatais, `session-bind@openssh.com`, `restrict`, `ChannelTimeout` e chaves FIDO (`ssh -Z`); consultado em 2026-10-03.
