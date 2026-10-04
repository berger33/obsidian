---
id: software.seguranca.tranche13.001203
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
relatorio_revisao_ia: "knowledge-federation/exports/reports/ai-review-software-seguranca-2000-0003-tranche-13.md"
fontes: ["https://raw.githubusercontent.com/keepassxreboot/keepassxc/develop/README.md", "https://keepassxc.org/docs/KeePassXC_UserGuide"]
tags: [dominio/software, subdominio/seguranca, qualidade/candidata]
lote: software-seguranca-2000-0003
---

# Integração Nativa com **`ssh-agent`** no KeePassXC: Carregamento Automático de Chaves SSH ao Destravar o Cofre e Remoção Automática no Lock

## Em uma frase
Como eliminar de vez os arquivos de chave privada SSH (`~/.ssh/id_ed25519`, `~/.ssh/id_rsa`) espalhados no sistema de arquivos do notebook, garantindo que suas chaves privadas SSH só existam descriptografadas na memória do `ssh-agent` enquanto o seu cofre KeePassXC estiver destravado?

## Por que importa
O KeePassXC possui uma integração nativa de primeira classe com o **`ssh-agent`** (no Linux/macOS via socket `SSH_AUTH_SOCK` e no Windows via OpenSSH Agent / Pageant): você anexa o arquivo da sua chave privada SSH diretamente como um **Anexo Criptografado (*Attachment*)** dentro de uma entrada do banco `.kdbx` (e apaga o arquivo original de `~/.ssh/` com `shred -u`), vai na aba **SSH Agent** da entrada e marca duas caixas fundamentais: **(1) *"Add key to agent when database is opened/unlocked"*** e **(2) *"Remove key from agent when database is closed/locked"***!

## Como funciona
Quando você destrava o KeePassXC pela manhã (com sua senha + YubiKey), o KeePassXC descriptografa a chave em memória e a injeta diretamente no `ssh-agent` (podendo ativar também `Confirm key usage (-c)` e tempo de expiração `-t`); e no exato segundo em que você bloqueia a tela do computador ou pressiona `Ctrl+L` no KeePassXC, **o KeePassXC remove automaticamente todas as chaves da memória do `ssh-agent`**!

## Exemplo
```bash
# Verificar com ssh-add -l que as chaves SSH aparecem no agente apenas quando o cofre KeePassXC esta aberto e somem ao bloquear (Ctrl+L)
ssh-add -l
```

## Limites e trade-offs
Você também pode adicionar (`Ctrl+H`) ou remover (`Ctrl+Shift+H`) manualmente a chave SSH da entrada selecionada para o `ssh-agent` a qualquer momento usando os atalhos de teclado nativos do KeePassXC.

## Como verificar
Combine esse fluxo com a opção *Lock database after inactivity* (ex.: 300 segundos) e *Lock database when session is locked or lid is closed* nas configurações de Segurança do KeePassXC.

## Conexões
- [[keepassxc-autenticacao-multifator-yubikey-hmac-sha1-keyfile]] — Veja também: Chave Composta do KeePassXC: Combinando **Senha Mestra + Key File + Hardware Challenge-Response (`YubiKey` / `OnlyKey` HMAC-SHA1)**.
- [[keepassxc-automacao-keepassxc-cli-scripts-ci-cd-extracao-segura]] — Veja também: Automação de Segredos no Terminal com **`keepassxc-cli`**: Injetando Credenciais e TOTPs em Variáveis de Ambiente sem Expor no `.bash_history`.
- [[keepassxc-arquitetura-cofre-offline-kdbx4-argon2id-chacha20-aes256]] — Referência cruzada direta com keepassxc-arquitetura-cofre-offline-kdbx4-argon2id-chacha20-aes256.
- [[openssh-seguranca-ssh-agent-destination-constraints-session-bind]] — Referência cruzada direta com openssh-seguranca-ssh-agent-destination-constraints-session-bind.

## Fontes
- [KeePassXC Official GitHub — Cross-Platform Community-Driven Port of Keepass](https://raw.githubusercontent.com/keepassxreboot/keepassxc/develop/README.md) — repositório oficial do KeePassXC cobrindo criptografia KDBX 4 (AES-256, Twofish, ChaCha20), YubiKey/OnlyKey, `keepassxc-cli`, SSH Agent e Secret Service; consultado em 2026-10-03.
- [KeePassXC Official User Guide (`keepassxc.org/docs/KeePassXC_UserGuide`)](https://keepassxc.org/docs/KeePassXC_UserGuide) — guia oficial do usuário do KeePassXC detalhando Auto-Type, integração com navegador, Passkeys, KeeShare, Database Reports (HIBP) e proteção de memória/tela; consultado em 2026-10-03.
