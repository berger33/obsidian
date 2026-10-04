---
id: software.seguranca.tranche13.001206
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

# Segurança do **Auto-Type (`Ctrl+Shift+V`)** no KeePassXC: Sequências Customizadas (`{USERNAME}{TAB}{PASSWORD}{TOTP}`), Delay e Validação de Título de Janela

## Em uma frase
Para aplicações que não rodam dentro do navegador Web (como clientes de terminal SSH, clientes RDP/VNC, consoles VMware/Proxmox, clientes VPN ou janelas de autenticação do sistema), copiar e colar senhas pelo Clipboard (`Ctrl+C` / `Ctrl+V`) deixa a senha exposta para qualquer processo em segundo plano que monitore a área de transferência!

## Por que importa
O recurso **Auto-Type (`Ctrl+Shift+V` ou Global Auto-Type)** do KeePassXC contorna completamente o Clipboard simulando eventos diretos de teclado para a janela alvo usando sequências configuráveis de placeholders como **`{USERNAME}{TAB}{PASSWORD}{ENTER}`**, **`{TOTP}`**, **`{DELAY 100}`** e atributos customizados **`{S:NomeDoAtributo}`**!

## Como funciona
Para impedir que o Auto-Type digite acidentalmente uma senha na janela errada (por exemplo, em um chat do Slack ou terminal compartilhado), configure na aba *Auto-Type* da entrada **Associações de Janela (*Window Associations*) com expressões regulares estritas sobre o título da janela** e habilite a confirmação **"Always ask before performing Auto-Type"**!

## Exemplo
```text
# Exemplo de sequencia Auto-Type customizada para login automatico que exige Usuario + Senha + pausa de 500ms + codigo TOTP de 6 digitos
{USERNAME}{TAB}{PASSWORD}{ENTER}{DELAY 500}{TOTP}{ENTER}
```

## Limites e trade-offs
Em sistemas Linux modernos rodando **Wayland** (onde o protocolo de isolamento gráfico impede por design que uma janela X11/Wayland injete teclas arbitrariamente em outra janela sem permissão do compositor), prefira a integração nativa **KeePassXC-Browser**, o **SSH Agent** embutido ou o **Secret Service (`freedesktop.org`)** para aplicações locais.

## Como verificar
Desde o KeePassXC 2.7.0+, a cópia de senha por duplo clique na tabela principal vem **desabilitada por padrão** justamente para evitar que um clique acidental envie segredos para o Clipboard do sistema.

## Conexões
- [[keepassxc-integracao-navegador-nativa-nacl-passkeys-anti-phishing]] — Veja também: Integração Segura com Navegadores (**`keepassxc-proxy`**) e Suporte a **Passkeys (WebAuthn / FIDO2)** no KeePassXC: Prevenção contra Phishing de Domínio.
- [[keepassxc-freedesktop-secret-service-substituicao-gnome-keyring-linux]] — Veja também: KeePassXC como Provedor **`org.freedesktop.secrets` (Secret Service D-Bus)** no Linux: Substituindo o `gnome-keyring` / `KWallet` com Criptografia Forte.
- [[keepassxc-arquitetura-cofre-offline-kdbx4-argon2id-chacha20-aes256]] — Referência cruzada direta com keepassxc-arquitetura-cofre-offline-kdbx4-argon2id-chacha20-aes256.

## Fontes
- [KeePassXC Official GitHub — Cross-Platform Community-Driven Port of Keepass](https://raw.githubusercontent.com/keepassxreboot/keepassxc/develop/README.md) — repositório oficial do KeePassXC cobrindo criptografia KDBX 4 (AES-256, Twofish, ChaCha20), YubiKey/OnlyKey, `keepassxc-cli`, SSH Agent e Secret Service; consultado em 2026-10-03.
- [KeePassXC Official User Guide (`keepassxc.org/docs/KeePassXC_UserGuide`)](https://keepassxc.org/docs/KeePassXC_UserGuide) — guia oficial do usuário do KeePassXC detalhando Auto-Type, integração com navegador, Passkeys, KeeShare, Database Reports (HIBP) e proteção de memória/tela; consultado em 2026-10-03.
