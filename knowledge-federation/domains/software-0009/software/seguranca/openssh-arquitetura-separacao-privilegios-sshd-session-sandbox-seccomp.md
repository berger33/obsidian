---
id: software.seguranca.tranche12.001191
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

# Arquitetura de Segurança do **OpenSSH (`openssh-portable`)**: Separação de Processos (`sshd`, `sshd-session`, `sshd-auth`) e Sandbox `seccomp` no Kernel

## Em uma frase
Como o **OpenSSH** — desenvolvido pelo projeto **OpenBSD** e mantido em sua edição portátil (`openssh-portable`) por Damien Miller, Darren Tucker e equipe — consegue expor uma porta de acesso remoto em milhões de servidores na internet mantendo um histórico de segurança extraordinário contra vulnerabilidades de corrupção de memória?

## Por que importa
O segredo está na sua arquitetura de **Separação Estrita de Privilégios (*Privilege Separation*)** combinada com **Desagregação de Binários** (introduzida a partir do OpenSSH 9.8 / 10.x): em vez de um único binário monolítico `/usr/sbin/sshd` carregar todo o código de escuta, criptografia pré-autenticação, PAM e sessão na memória RAM com o mesmo layout de endereço (`ASLR`), o OpenSSH divide o trabalho em executáveis separados!

## Como funciona
O daemon principal **`sshd`** apenas aceita conexões TCP; para cada conexão, ele invoca um novo binário **`sshd-session`** (e **`sshd-auth`** para a fase de pré-autenticação), onde o processo que conversa com a rede roda **sem privilégios (`user sshd`), preso em um `chroot("/var/empty")` e confinado por um filtro estrito de syscalls `seccomp-bpf` e `NO_NEW_PRIVS` do kernel** (que desde o OpenSSH 10.4 aborta fatalmente a inicialização caso o kernel falhe em ativar o `seccomp`!)!

## Exemplo
```bash
# Inspecionar a arvore de processos separados do OpenSSH (sshd listener e sshd-session monitor/worker) e validar a configuracao
ps -ef | grep sshd
sudo sshd -T | grep -E "^(usepam|kbdinteractiveauthentication|passwordauthentication|permitrootlogin)"
```

## Limites e trade-offs
Por que separar o ouvinte `sshd` do `sshd-session` / `sshd-auth` em binários distintos foi um marco de engenharia defensiva? Porque cada nova conexão executa `execve()` em um binário recém-carregado com **um novo sorteio aleatório de ASLR (*Address Space Layout Randomization*)**, impedindo que um atacante que cause um crash em um processo filho descubra os endereços de memória da `libc` nos próximos processos!

## Como verificar
No OpenSSH 10.4+, lembre-se de que o comando de despejo de configuração efetiva (**`sshd -G`** ou **`sshd -T`**) emite as diretivas em *MixedCase* (`PubkeyAuthentication`) para consistência.

## Conexões
- [[openssh-criptografia-pos-quantica-kex-mlkem768-sntrup761-chacha20]] — Veja também: Criptografia **Pós-Quântica Híbrida** no OpenSSH: Key Exchange **`mlkem768x25519-sha256`** e **`sntrup761x25519-sha512`**, Cifras AEAD e MACs `etm`.
- [[openssh-hardening-sshd-config-criptografia-autenticacao-restricoes]] — Referência cruzada direta com openssh-hardening-sshd-config-criptografia-autenticacao-restricoes.
- [[aide-resposta-incidentes-forense-linux-rootkits-ld-so-preload-pam]] — Referência cruzada direta com aide-resposta-incidentes-forense-linux-rootkits-ld-so-preload-pam.

## Fontes
- [OpenSSH Portable Official Repository README (`openssh/openssh-portable`)](https://raw.githubusercontent.com/openssh/openssh-portable/master/README) — documentação oficial do OpenSSH Portable detalhando a arquitetura derivada do OpenBSD, suporte a PAM/libcrypto e diretrizes de segurança; consultado em 2026-10-03.
- [OpenSSH Official Release Notes (OpenSSH 10.4 / 10.5p1)](https://www.openssh.com/releasenotes.html) — notas de lançamento oficiais do OpenSSH detalhando melhorias de segurança em `sshd-session`, `seccomp`/`NO_NEW_PRIVS` fatais, `session-bind@openssh.com`, `restrict`, `ChannelTimeout` e chaves FIDO (`ssh -Z`); consultado em 2026-10-03.
