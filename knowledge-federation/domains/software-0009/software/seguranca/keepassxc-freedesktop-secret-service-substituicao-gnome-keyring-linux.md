---
id: software.seguranca.tranche13.001207
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

# KeePassXC como Provedor **`org.freedesktop.secrets` (Secret Service D-Bus)** no Linux: Substituindo o `gnome-keyring` / `KWallet` com Criptografia Forte

## Em uma frase
Em estações de trabalho Linux de desenvolvedores e engenheiros de segurança, dezenas de aplicações (como `git-credential-libsecret`, `NetworkManager`, clientes VPN, VS Code, clientes de e-mail e CLIs de nuvem) armazenam tokens OAuth e senhas através da API padrão D-Bus **`org.freedesktop.secrets` (FreeDesktop.org Secret Service)**.

## Por que importa
O problema do `gnome-keyring` padrão é que ele é destravado automaticamente no login da sessão gráfica com a mesma senha do usuário Linux e permanece aberto durante todo o dia sem exigir YubiKey nem bloqueio por inatividade independente!

## Como funciona
Ao habilitar a integração **Secret Service (`Tools` -> `Settings` -> `Secret Service Integration`)** no KeePassXC e expor um grupo específico do seu banco `.kdbx` no barramento D-Bus `org.freedesktop.secrets`, **o próprio KeePassXC assume o papel de Keyring do sistema operacional Linux** — protegendo todos os segredos das aplicações locais sob a criptografia **Argon2id + ChaCha20 + YubiKey** do seu cofre KDBX 4 e exigindo confirmação a cada acesso!

## Exemplo
```bash
# Consultar e armazenar um segredo de teste usando secret-tool (libsecret) diretamente no grupo exposto pelo KeePassXC via D-Bus
secret-tool store --label="Token-API-Homolog" servico api-interna usuario devops
secret-tool lookup servico api-interna usuario devops
```

## Limites e trade-offs
Para evitar conflito no barramento D-Bus `org.freedesktop.secrets`, lembre-se de que apenas um daemon de Secret Service pode responder por vez na sessão do usuário (você pode desativar o componente `secrets` do `gnome-keyring-daemon` ao habilitar o Secret Service no KeePassXC).

## Como verificar
Exponha apenas um subgrupo dedicado (ex.: `/Linux-Secret-Service`) do seu banco `.kdbx` para a API D-Bus, mantendo o restante das pastas críticas de produção invisíveis para aplicações locais no D-Bus!

## Conexões
- [[keepassxc-autotype-sequencias-customizadas-protecao-window-title]] — Veja também: Segurança do **Auto-Type (`Ctrl+Shift+V`)** no KeePassXC: Sequências Customizadas (`{USERNAME}{TAB}{PASSWORD}{TOTP}`), Delay e Validação de Título de Janela.
- [[keepassxc-compartilhamento-equipes-keeshare-assinatura-merge-git]] — Veja também: Compartilhamento Seguro de Cofres em Equipe com **KeeShare** (Contêineres Assinados) e Resolução de Conflitos com **`keepassxc-cli merge`**.
- [[keepassxc-arquitetura-cofre-offline-kdbx4-argon2id-chacha20-aes256]] — Referência cruzada direta com keepassxc-arquitetura-cofre-offline-kdbx4-argon2id-chacha20-aes256.
- [[keepassxc-integracao-ssh-agent-chaves-privadas-anexos-lock]] — Referência cruzada direta com keepassxc-integracao-ssh-agent-chaves-privadas-anexos-lock.
- [[keepassxc-automacao-keepassxc-cli-scripts-ci-cd-extracao-segura]] — Referência cruzada direta com keepassxc-automacao-keepassxc-cli-scripts-ci-cd-extracao-segura.

## Fontes
- [KeePassXC Official GitHub — Cross-Platform Community-Driven Port of Keepass](https://raw.githubusercontent.com/keepassxreboot/keepassxc/develop/README.md) — repositório oficial do KeePassXC cobrindo criptografia KDBX 4 (AES-256, Twofish, ChaCha20), YubiKey/OnlyKey, `keepassxc-cli`, SSH Agent e Secret Service; consultado em 2026-10-03.
- [KeePassXC Official User Guide (`keepassxc.org/docs/KeePassXC_UserGuide`)](https://keepassxc.org/docs/KeePassXC_UserGuide) — guia oficial do usuário do KeePassXC detalhando Auto-Type, integração com navegador, Passkeys, KeeShare, Database Reports (HIBP) e proteção de memória/tela; consultado em 2026-10-03.
