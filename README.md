# OpenCode Go para Home Assistant

Integração customizada para usar a **API OpenCode Go** como agente de conversa no Home Assistant.

Baseada no componente oficial Open Router, com endpoint atualizado para a API v2 do OpenCode Go.

---

## O que é

O [OpenCode Go](https://opencode.ai/docs/go) é um plano de acesso a modelos de código populares via API OpenAI-compatible. Esta integração permite usar esses modelos dentro do assistente do Home Assistant.

> **Atenção:** o OpenCode Go requer uma assinatura ativa (Go ou Go Plus) e uma API key gerada no Console do OpenCode.

---

## Funcionalidades

- Agente de conversa usando modelos OpenCode Go
- Suporte às ferramentas nativas do Home Assistant (`Assist`, controle de dispositivos, etc.)
- Geração de dados estruturados via AI Task
- Configuração 100% pela UI (config flow)

---

## Instalação

### Via HACS

1. Adicione este repositório como repositório customizado no HACS:
   - URL: `https://github.com/wesiofilhoIF/opencodeGO_ha`
   - Categoria: **Integration**
2. Procure por **OpenCode** na loja do HACS e instale.
3. Reinicie o Home Assistant.

### Manual

1. Baixe o código deste repositório.
2. Copie a pasta `custom_components/open_code` para dentro da pasta `custom_components/` da sua instalação Home Assistant.
3. Reinicie o Home Assistant.

---

## Configuração

1. No Home Assistant, vá em **Configurações > Dispositivos e serviços**.
2. Clique em **Adicionar integração**.
3. Procure por **OpenCode**.
4. Insira sua **API Key** do OpenCode Go.
5. Após a integração principal ser criada, adicione uma subentrada:
   - **Conversation agent** → para usar no Assist
   - **AI task** → para geração de dados em automações/scripts
6. Selecione o modelo desejado e finalize.

---

## Gerar API Key

1. Acesse o [OpenCode Console](https://opencode.ai/console) e faça login.
2. Assine o plano **OpenCode Go** ou **Go Plus**.
3. Vá em **API Keys** nas configurações do workspace.
4. Crie uma nova chave e copie o valor.

> A API key é necessária para todos os modelos pagos. Modelos gratuitos podem ter restrições de uso fora do ambiente OpenCode.

---

## Modelos suportados (sujeitos a alteração)

A lista de modelos é obtida automaticamente da API. Entre os disponíveis atualmente no OpenCode Go estão:

- Grok 4.7 / 4.6
- GLM-5.3 / GLM-5.3-Flash / GLM-5.2
- GPT 6 Luna / GPT 5.6 Luna
- Claude Haiku 5.5
- Kimi K3 / Kimi K2.7 Code / Kimi K2.6
- LongCat-2.0 / LongCat 2.5 Preview Free
- MiMo-V2.6 / MiMo-V2.5
- MiniMax M3 / M2.7
- Muse Spark 1.3 / 1.2 Contributor
- Qwen3.8 Max / Flash / Qwen3.7 Plus
- DeepSeek V4.1 / V4 Pro / V4 Flash
- Hy4 preview / Hy3 / Space Bunny

Consulte a [documentação oficial](https://opencode.ai/docs/go) para a lista atual, preços e limites de uso.

---

## Endpoint

```text
Base URL: https://opencode.ai/zen/go/v1
```

A integração usa a API OpenAI-compatible do OpenCode Go.

---

## Remover a integração

1. Vá em **Configurações > Dispositivos e serviços**.
2. Selecione o card da integração OpenCode.
3. Clique nos três pontos ao lado da entrada desejada e selecione **Excluir**.

---

## Solução de problemas

- **Erro de autenticação:** verifique se a API key está correta e se a assinatura Go/Go Plus está ativa.
- **Nenhum modelo carrega:** confirme se a integração principal foi carregada com sucesso e se há conectividade com `https://opencode.ai`.
- **Modelo não responde:** alguns modelos exigem parâmetros específicos (ex: `max_tokens` na família Anthropic). Teste outro modelo primeiro.

Para logs de debug, adicione ao `configuration.yaml`:

```yaml
logger:
  logs:
    custom_components.open_code: debug
```

---

## Links

- Repositório: https://github.com/wesiofilhoIF/opencodeGO_ha
- Documentação OpenCode Go: https://opencode.ai/docs/go
- Console OpenCode: https://opencode.ai/console
